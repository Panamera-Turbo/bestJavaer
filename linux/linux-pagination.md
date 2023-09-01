# Linux 分页机制

[toc]

分页机制是 80x86 内存管理机制的第二种机制，分段机制用于把虚拟地址转换为线性地址，而分页机制用于把线性地址转换为物理地址。分页机制可以用于任何一种分段机制，也可以理解为先有分段机制才有分页机制，这是由于历史原因，分段机制要比分页机制更轻，先出现的分段后出现的分页。

处理器的分页机制用于把线性地址划分成一个个的页面，这些划分成页面的线性地址会被映射到物理空间的页面上。

>我们知道分段的保护措施有两种，一种是利用任务之间的保护；一种是利用内存段和寄存器之间的保护。

分页机制有几种页面级的保护措施，分段机制和保护措施可以和分页机制的保护措施一起使用，也可以使用分页机制的保护措施替换分段机制的保护。

比如分页机制可以在页面的基础上加强读/写保护。另外，在页面单元上，分页机制还提供了用户和超级用户两级保护。

分页机制可以通过 CR0 控制寄存器的 PG 这个标志位来判断是否开启分页机制；如果 PG = 1 ，则表示启用分页操作，处理器会使用本节描述的机制将线性地址转换为物理地址。如果 PG = 0，则表示禁用分页机制，此时分段产生的线性地址会被直接用作物理地址。

分段机制和分页机制还有一个区别就是：分段机制可以在任意可变长度的内存上进行操作，而分页机制只能对固定大小的页面（内存块）进行操作。分页机制把线性和物理地址空间都划分成页面。线性地址空间中的页面都可以映射在物理地址空间内，如下图所示。

![](https://www.cxuan.vip/image-20230423081456896.png)

80x86 使用 4K (2 ^ 12) 字节固定大小的页面，每个页面均是 4KB，并且对齐于 4KB 地址边界处。这表示分页机制会把 4GB 划分成为以 4KB 为基础的页面，共划分 1M（1048576） 个，线性地址的低 12 bit 位可以直接作为页内偏移量，也可直接作为物理地址的低 12 位。

现在我们知道线性地址空间会经过分页机制映射到物理内存空间上，这是一个正常能够映射到的情况，如果映射不到怎么办？也就是说包含线性地址空间的页面不在物理内存中怎么办？此时处理器就会产生一个页错误异常。页错误异常的处理程序会让操作系统从磁盘中把相应的页面加载到物理内存中。当页面加载到物理内存中后，会从异常处理程序中返回，使得处于异常指令的位置继续向下执行指令。

页错误异常是分页机制实现换入换出过程中出现频次非常高的一种异常机制，它就好像 bug 一样如影随形，而且频繁的页面换入换出操作会很耗费处理器资源，所以为了减少频繁换入换出的操作，采用了一种**局部性原理**的方式：把经常访问的页目录和相关页 "保存" 起来，这里采用了一种硬件实现，即**转换查找缓冲区（Translation Lookaside Buffer）**。有了 TLB，处理器会先从 TLB 中查找相关页，TLB 中不存在的页才会从内存中进行读取，此时的 TLB 相当于是内存的一个副本。

## 页表结构

页表中每个页表项的大小为 32 位，其中 20 位来存放物理基地址，剩余的 12 位存放可用于存放页面是否存在等属性信息。如果线性地址索引的页表项被标注为存在，则表示该项有效，我们可以从中取得物理地址；如果线性地址索引的页表项不存在，那么访问物理页面就会产生异常。

下面是一个线性地址到物理地址的变换过程图。

![](https://www.cxuan.vip/image-20230424212210249.png)

可以看到，80x86 使用了两级页，这是为了减少页的数量所设计的，因为虽然每个页字节是 4K，共有 2 ^ 20 （1MB）个页，总共占据 4MB 大小，但实际上应用程序一次用不到这么多页，会造成资源浪费，所以采用了一种分层的设计方式。

第一级称为**页目录（page directory）**，它被存放在 1 个 4K 页面中，因为一共有 2 ^ 10 次方（1 MB）个页目录，每个目录是 4 字节，所以是在一个 4K 页面中。线性地址的最高十位（22 - 31 位）用作一级表（页目录）中的索引来访问二级表。

第二级称为**页表（page table）**，它和页目录一样，也是占据一个页面，最多含有 1K 个 4 字节的页表。页表项会存储 20 位的物理地址，线性地址中的 12 - 21 位作为页表的索引，用于获取含有 20 位物理地址的页表项。页表项的 20 位物理基地址和线性地址中的低 12 位一起合成最终的 32 位物理地址。

## 页表项结构

现在我们知道线性地址的低 12 位和页表存储的 20 位可以合成物理地址，页表项除了能够存储地址外，还有一些其他的属性，下面是页表项的结构图。

>这里需要特别注意的是，页目录的结构和页表的结构是一样的，只不过他俩描述的主体不一样，一个描述的是页目录，一个描述的是页表。

![](https://www.cxuan.vip/image-20230425112420861.png)

* P -- 位 0 是存在（Present）标志，用于指明表项对地址转换是否有效。P = 1 表示有效，P = 0 表示无效，在页的转换过程中，如果说涉及的页目录或页表的表项无效，也就是页面没有再物理地址中，就会产生一个异常。如果 P = 0 ，那么除了表项无效外，其余的 bit 位可以自由使用。
* R/W -- 位 1 是读/写（Read/Write）标志，当 R/W = 1 时，表示该页可以被读、写和执行；当 R/W = 0 时，表示该页只读或可执行；当处理器运行在超级用户权限下（0、1、2）时，此位不会发生作用。
* U/S -- 位 2 是用户/超级用户（User/Supervisor）标识，如果此位为 0 ，表示任意特权级下面的应用程序都可以访问，如果此位为 1 ，那么页面只能允许在特权级为 0、1、2 也就是超级用户特权级下才能访问。
* A -- 位 5 是已访问（Accessed）标志，此位仅用于统计页面的访问情况，如果页面已经访问过，就会置 1，但是操作系统会通过定期复位来重置此标识位。
* D -- 位 6 是页面已修改（Dirty）标志，也就是我们常说的"脏位"，当处理器对页面执行写操作时，就会设置对应页面的 D 标志。
* AVL -- 保留字段，这个字段专门提供给程序使用。

根据上面字段的描述，可以看到页目录和页表项中的 P 位为分页技术的虚拟存储提供了必要的标识，若线性地址空间中的页面存在于物理内存中，那么对应的表项 P = 1，并且该表项中含有相应的物理地址。页面不在物理内存中的表项 P = 0 。如果程序访问物理内存中不存在的页面，处理器就会产生一个缺页异常。此时操作系统就会利用这个异常把缺少的页面从磁盘调入内存，把相应的物理地址放在表项中，返回程序继续执行引起异常的指令并且设置 P = 1。

A 和 D 这两个标志位是实现虚拟存储的基础，这两个标志位可以定期检测指定的页面是否访问过并且是否可以读写，从而判断哪些页面可以移出到磁盘。比如一个页面从磁盘读入内存后，它的 D 标志位为 0 ，那么当页被移除磁盘时，它的 D 位还是 0 的话，就可以判断这个页面无需调入磁盘。D = 1 表示页面已经被修改过，就需要将其写回到磁盘上。
