(function () {
  var articleIndexCache = {};
  var coverCache = new Map();
  var renderTimer = 0;
  var sidebarTimer = 0;
  var activeSidebarLocale = 'en';
  var sidebarLinks = [
    {
      enHref: '#/',
      enText: 'Home',
      zhHref: '#/README.zh-CN',
      zhText: '首页'
    },
    {
      enHref: '#/README.zh-CN',
      enText: 'Chinese README',
      zhHref: '#/',
      zhText: '英文 README'
    },
    {
      enHref: '#/en/ai-articles/README',
      enText: 'AI Articles',
      zhHref: '#/ai-articles/README',
      zhText: 'AI 文章'
    },
    {
      enHref: '#/en/ai-articles/01-agent-and-coding/README',
      enText: 'AI Agent & Coding Tools',
      zhHref: '#/ai-articles/01-agent-and-coding/README',
      zhText: 'AI Agent 与编程工具'
    },
    {
      enHref: '#/en/ai-articles/02-models-and-research/README',
      enText: 'Models, Research & Prompt',
      zhHref: '#/ai-articles/02-models-and-research/README',
      zhText: '模型、研究与 Prompt'
    },
    {
      enHref: '#/en/ai-articles/03-tools-and-resources/README',
      enText: 'Tools, Resources & Workbench',
      zhHref: '#/ai-articles/03-tools-and-resources/README',
      zhText: '工具、资源与工作台'
    },
    {
      enHref: '#/en/ai-articles/04-industry-and-business/README',
      enText: 'Industry, Companies & Business',
      zhHref: '#/ai-articles/04-industry-and-business/README',
      zhText: '产业、公司与商业动态'
    },
    {
      enHref: '#/en/ai-articles/05-ai-creation-and-media/README',
      enText: 'AI Creation & Media',
      zhHref: '#/ai-articles/05-ai-creation-and-media/README',
      zhText: 'AI 生成与多媒体'
    },
    {
      enHref: '#/en/ai-articles/06-notes-and-observations/README',
      enText: 'Notes, Essays & Incidents',
      zhHref: '#/ai-articles/06-notes-and-observations/README',
      zhText: '观察、杂谈与事故记录'
    },
    {
      enHref: '#/en/ai-resources/README',
      enText: 'AI Resources',
      zhHref: '#/ai-resources/README',
      zhText: 'AI 资源'
    },
    {
      enHref: '#/en/works/README',
      enText: 'Works & Open Source',
      zhHref: '#/works/README',
      zhText: '我的作品 & 开源项目'
    },
    {
      enHref: '#/en/development-guidelines/README',
      enText: 'Development Guidelines',
      zhHref: '#/development-guidelines/README',
      zhText: '开发规约'
    },
    {
      enHref: '#/archive-bestjavaer/README',
      enText: 'archive-bestjavaer',
      zhHref: '#/archive-bestjavaer/README',
      zhText: '旧 bestJavaer'
    }
  ];
  var sidebarGroupLabels = [
    {
      enText: 'Main Track',
      zhText: '新主线'
    },
    {
      enText: 'Legacy Archive',
      zhText: '旧内容归档'
    }
  ];

  window.$docsify = window.$docsify || {};
  window.$docsify.plugins = (Array.isArray(window.$docsify.plugins) ? window.$docsify.plugins : []).concat(function articleCardsPlugin(hook) {
    hook.doneEach(function () {
      scheduleRender();
      scheduleSidebarLocalization();
    });
  });

  startStandaloneRenderer();

  function startStandaloneRenderer() {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', function () {
        scheduleRender();
        scheduleSidebarLocalization();
      });
    } else {
      scheduleRender();
      scheduleSidebarLocalization();
    }

    [250, 750, 1500, 3000].forEach(function (delay) {
      window.setTimeout(scheduleRender, delay);
      window.setTimeout(scheduleSidebarLocalization, delay);
    });

    window.addEventListener('hashchange', function () {
      scheduleRender();
      scheduleSidebarLocalization();
      window.setTimeout(scheduleRender, 250);
      window.setTimeout(scheduleSidebarLocalization, 250);
    });

    var observer = new MutationObserver(function (mutations) {
      var shouldRender = mutations.some(function (mutation) {
        var target = mutation.target;

        return (
          target.nodeType === 1 &&
          (
            target.classList.contains('markdown-section') ||
            target.classList.contains('content') ||
            target.querySelector && target.querySelector('.markdown-section')
          )
        );
      });
      var shouldLocalizeSidebar = mutations.some(function (mutation) {
        var target = mutation.target;

        return (
          target.nodeType === 1 &&
          (
            target.classList.contains('sidebar') ||
            target.classList.contains('sidebar-nav') ||
            target.querySelector && target.querySelector('.sidebar-nav')
          )
        );
      });

      if (shouldRender) {
        scheduleRender();
      }

      if (shouldLocalizeSidebar) {
        scheduleSidebarLocalization();
      }
    });

    observer.observe(document.documentElement, {
      childList: true,
      subtree: true
    });
  }

  function scheduleRender() {
    window.clearTimeout(renderTimer);
    renderTimer = window.setTimeout(renderArticleCards, 50);
  }

  function scheduleSidebarLocalization() {
    window.clearTimeout(sidebarTimer);
    sidebarTimer = window.setTimeout(localizeSidebar, 50);
  }

  function localizeSidebar() {
    var sidebar = document.querySelector('.sidebar-nav');
    var route = getCurrentRoute();
    var locale = getSidebarLocale(route);
    var handledLinks = [];

    if (!sidebar) {
      return;
    }

    sidebarLinks.forEach(function (item) {
      var link = findSidebarLink(sidebar, item, handledLinks);

      if (!link) {
        return;
      }

      link.textContent = locale === 'zh' ? item.zhText : item.enText;
      link.setAttribute('href', locale === 'zh' ? item.zhHref : item.enHref);
      handledLinks.push(link);
    });

    localizeSidebarGroupLabels(sidebar, locale);
    syncSidebarActiveState(sidebar, route, locale);
  }

  function getSidebarLocale(route) {
    var normalizedRoute = normalizeRoute(route);

    if (
      normalizedRoute === 'README.zh-CN' ||
      normalizedRoute === 'ai-articles' ||
      normalizedRoute.indexOf('ai-articles/') === 0 ||
      normalizedRoute === 'ai-resources' ||
      normalizedRoute.indexOf('ai-resources/') === 0 ||
      normalizedRoute === 'works' ||
      normalizedRoute.indexOf('works/') === 0 ||
      normalizedRoute === 'development-guidelines' ||
      normalizedRoute.indexOf('development-guidelines/') === 0
    ) {
      activeSidebarLocale = 'zh';
      return activeSidebarLocale;
    }

    if (
      normalizedRoute === '' ||
      normalizedRoute === '/' ||
      normalizedRoute === 'README' ||
      normalizedRoute.indexOf('en/') === 0
    ) {
      activeSidebarLocale = 'en';
      return activeSidebarLocale;
    }

    return activeSidebarLocale;
  }

  function findSidebarLink(sidebar, item, handledLinks) {
    var hrefs = [item.enHref, item.zhHref].map(normalizeHashHref);
    var texts = [item.enText, item.zhText];

    return Array.from(sidebar.querySelectorAll('a[href]')).find(function (link) {
      var href = normalizeHashHref(link.getAttribute('href') || '');
      var text = link.textContent.trim();

      return handledLinks.indexOf(link) === -1 && (hrefs.indexOf(href) !== -1 || texts.indexOf(text) !== -1);
    });
  }

  function localizeSidebarGroupLabels(sidebar, locale) {
    var replacements = {};

    sidebarGroupLabels.forEach(function (label) {
      replacements[label.enText] = locale === 'zh' ? label.zhText : label.enText;
      replacements[label.zhText] = locale === 'zh' ? label.zhText : label.enText;
    });

    Array.from(sidebar.querySelectorAll('li')).forEach(function (item) {
      Array.from(item.childNodes).some(function (node) {
        var text = node.textContent ? node.textContent.trim() : '';

        if (node.nodeType === 3 && replacements[text]) {
          node.textContent = replacements[text];
          return true;
        }

        if (node.nodeType === 1 && node.tagName === 'P' && replacements[text]) {
          node.textContent = replacements[text];
          return true;
        }

        return false;
      });
    });
  }

  function syncSidebarActiveState(sidebar, route, locale) {
    var activeHref = getActiveSidebarHref(route, locale);

    Array.from(sidebar.querySelectorAll('li.active')).forEach(function (item) {
      item.classList.remove('active');
    });

    if (!activeHref) {
      return;
    }

    Array.from(sidebar.querySelectorAll('a[href]')).forEach(function (link) {
      if (normalizeHashHref(link.getAttribute('href') || '') !== activeHref) {
        return;
      }

      var item = link.closest('li');

      while (item && sidebar.contains(item)) {
        item.classList.add('active');
        item = item.parentElement ? item.parentElement.closest('li') : null;
      }
    });
  }

  function getActiveSidebarHref(route, locale) {
    var normalizedRoute = normalizeRoute(route);

    if (normalizedRoute === '' || normalizedRoute === '/' || normalizedRoute === 'README') {
      return normalizeHashHref('#/');
    }

    if (normalizedRoute === 'README.zh-CN') {
      return normalizeHashHref('#/README.zh-CN');
    }

    if (!/\/README$/.test(normalizedRoute) && normalizedRoute.indexOf('/') > -1) {
      normalizedRoute = normalizedRoute.replace(/\/[^/]+$/, '/README');
    }

    if (locale === 'zh' && normalizedRoute.indexOf('en/') === 0) {
      normalizedRoute = normalizedRoute.replace(/^en\//, '');
    }

    return normalizeHashHref('#/' + normalizedRoute);
  }

  function normalizeHashHref(href) {
    var cleanHref = (href || '').trim();

    if (cleanHref.indexOf('#/') > -1) {
      cleanHref = '#/' + cleanHref.split('#/')[1];
    }

    cleanHref = cleanHref.split('?')[0].replace(/\.md$/i, '').replace(/\/+$/, '');

    if (cleanHref === '#') {
      cleanHref = '#/';
    }

    try {
      cleanHref = decodeURIComponent(cleanHref);
    } catch (error) {
      return cleanHref;
    }

    return cleanHref || '#/';
  }

  function normalizeRoute(route) {
    var normalized = (route || '').replace(/^\/+/, '').replace(/\.md$/i, '').replace(/\/+$/, '');

    try {
      normalized = decodeURIComponent(normalized);
    } catch (error) {
      return normalized;
    }

    return normalized;
  }

  function renderArticleCards() {
    var route = getCurrentRoute();
    var isHome = isHomeRoute(route);
    var isArticleIndex = isArticleIndexRoute(route);
    var currentMarkdownPath = getCurrentMarkdownPath(route);
    var isArticleDetail = isArticleMarkdown(currentMarkdownPath);

    document.documentElement.classList.toggle('home-page', isHome);
    document.documentElement.classList.toggle('article-index-page', isArticleIndex);
    document.documentElement.classList.toggle('article-detail-page', isArticleDetail);
    document.documentElement.classList.toggle('wide-page', isHome || isArticleIndex);

    var section = document.querySelector('.markdown-section');

    if (!section) {
      return;
    }

    if (isHome) {
      decorateHomePage(section);
    }

    if (isArticleDetail) {
      renderSeriesNav(section, currentMarkdownPath);
    }

    if (!isArticleIndex) {
      return;
    }

    Array.from(section.querySelectorAll('ul')).forEach(function (list) {
      var items = Array.from(list.children).filter(function (item) {
        return item.tagName === 'LI';
      });
      var articleItems = items.map(toArticleItem).filter(Boolean);

      if (articleItems.length < 2) {
        return;
      }

      list.classList.add('article-card-grid');
      articleItems.forEach(function (item) {
        renderCard(item);
      });
    });
  }

  function renderSeriesNav(section, currentMarkdownPath) {
    if (section.querySelector('.article-series-nav')) {
      return;
    }

    var articleRoot = currentMarkdownPath.indexOf('en/ai-articles/') === 0 ? 'en/ai-articles' : 'ai-articles';
    var isEnglishArticle = articleRoot === 'en/ai-articles';

    getArticleIndex(articleRoot).then(function (articles) {
      var activePath = getCurrentMarkdownPath(getCurrentRoute());
      var index = articles.findIndex(function (article) {
        return normalizeMarkdownPath(article.markdownPath) === normalizeMarkdownPath(currentMarkdownPath);
      });

      if (normalizeMarkdownPath(activePath) !== normalizeMarkdownPath(currentMarkdownPath) || index < 0) {
        return;
      }

      var previous = articles[index - 1] || null;
      var next = articles[index + 1] || null;

      if (!previous && !next) {
        return;
      }

      var nav = document.createElement('div');

      nav.className = 'article-series-nav';
      nav.setAttribute('aria-label', isEnglishArticle ? 'Article series navigation' : '文章连载导航');
      nav.setAttribute('role', 'navigation');
      nav.appendChild(createSeriesCard(previous, isEnglishArticle ? 'Previous' : '上一篇', isEnglishArticle ? 'This is the first article' : '已经是第一篇', 'previous'));
      nav.appendChild(createSeriesCard(next, isEnglishArticle ? 'Next' : '下一篇', isEnglishArticle ? 'This is the last article' : '已经是最后一篇', 'next'));
      section.appendChild(nav);
    });
  }

  function createSeriesCard(article, label, fallbackTitle, direction) {
    var card = document.createElement(article ? 'a' : 'span');
    var labelNode = document.createElement('span');
    var titleNode = document.createElement('span');
    var dateNode = document.createElement('span');

    card.className = 'article-series-card is-' + direction + (article ? '' : ' is-disabled');

    if (article) {
      card.href = article.href;
    }

    labelNode.className = 'article-series-card-label';
    titleNode.className = 'article-series-card-title';
    dateNode.className = 'article-series-card-date';
    labelNode.textContent = label;
    titleNode.textContent = article ? article.title : fallbackTitle;
    dateNode.textContent = article && article.date ? article.date : '';

    card.appendChild(labelNode);
    card.appendChild(titleNode);
    card.appendChild(dateNode);

    return card;
  }

  function getArticleIndex(articleRoot) {
    articleRoot = articleRoot || 'ai-articles';

    if (articleIndexCache[articleRoot]) {
      return articleIndexCache[articleRoot];
    }

    articleIndexCache[articleRoot] = fetch(articleRoot + '/README.md?v=20260604-bilingual-readme', {
      cache: 'force-cache'
    })
      .then(function (response) {
        if (!response.ok) {
          return '';
        }

        return response.text();
      })
      .then(function (markdown) {
        return extractArticleIndex(markdown, articleRoot);
      })
      .catch(function () {
        return [];
      });

    return articleIndexCache[articleRoot];
  }

  function extractArticleIndex(markdown, articleRoot) {
    var articles = [];
    var pattern = /^\s*-\s*(\d{4}-\d{2}-\d{2})\s*-\s*\[([^\]]+)\]\(([^)]+)\)/gm;
    var match;

    while ((match = pattern.exec(markdown))) {
      var markdownPath = resolveIndexMarkdownPath(match[3], articleRoot);

      if (!isArticleMarkdown(markdownPath)) {
        continue;
      }

      articles.push({
        date: match[1],
        href: toRouteHref(markdownPath),
        markdownPath: markdownPath,
        title: match[2].trim()
      });
    }

    return articles;
  }

  function resolveIndexMarkdownPath(href, articleRoot) {
    articleRoot = articleRoot || 'ai-articles';

    var cleanHref = (href || '').split('?')[0].split('#')[0].trim();

    if (!cleanHref || /^(https?:|mailto:)/i.test(cleanHref)) {
      return '';
    }

    if (cleanHref.indexOf('#/') === 0) {
      return toMarkdownPath(cleanHref);
    }

    if (cleanHref.indexOf('./') === 0) {
      cleanHref = articleRoot + '/' + cleanHref.slice(2);
    } else if (cleanHref.indexOf(articleRoot + '/') !== 0) {
      cleanHref = articleRoot + '/' + cleanHref.replace(/^\/+/, '');
    }

    if (!/\.md$/i.test(cleanHref)) {
      cleanHref += '.md';
    }

    return cleanHref.replace(/^\/+/, '');
  }

  function decorateHomePage(section) {
    var latestArticles = collectHomeUpdateArticles(section).slice(0, 6);
    var classes = [
      'home-reading-grid',
      'home-feature-grid',
      'home-update-list',
      'home-reason-grid'
    ];
    var classByHeading = {
      '先从这几篇开始': 'home-reading-grid',
      'Start Here': 'home-reading-grid',
      '新主线': 'home-feature-grid',
      'Main Sections': 'home-feature-grid',
      '最近更新': 'home-update-list',
      'Recent Updates': 'home-update-list',
      '为什么值得关注': 'home-reason-grid',
      'Why Follow': 'home-reason-grid'
    };

    Array.from(section.querySelectorAll('h2')).forEach(function (heading) {
      var listClass = classByHeading[heading.textContent.trim()];
      var next = heading.nextElementSibling;

      if (!listClass || !next || next.tagName !== 'UL') {
        return;
      }

      classes.forEach(function (className) {
        next.classList.remove(className);
      });
      next.classList.add(listClass);

      if (listClass === 'home-reading-grid') {
        renderFeaturedCards(next, latestArticles);
      }

      if (listClass === 'home-feature-grid') {
        renderFeatureCards(next);
      }
    });
  }

  function collectHomeUpdateArticles(section) {
    var updateHeadings = ['最近更新', 'Recent Updates'];
    var updateList = Array.from(section.querySelectorAll('h2')).reduce(function (found, heading) {
      if (found || updateHeadings.indexOf(heading.textContent.trim()) === -1) {
        return found;
      }

      return heading.nextElementSibling && heading.nextElementSibling.tagName === 'UL' ? heading.nextElementSibling : null;
    }, null);

    if (!updateList) {
      return [];
    }

    return Array.from(updateList.children).map(toHomeUpdateItem).filter(Boolean);
  }

  function toHomeUpdateItem(listItem) {
    if (!listItem || listItem.tagName !== 'LI') {
      return null;
    }

    var link = listItem.querySelector('a[href]');

    if (!link) {
      return null;
    }

    var markdownPath = toMarkdownPath(link.getAttribute('href') || '');

    if (!markdownPath || !isArticleMarkdown(markdownPath)) {
      return null;
    }

    var rawText = listItem.textContent.replace(/\s+/g, ' ').trim();
    var dateMatch = rawText.match(/^(\d{4}-\d{2}-\d{2})\s*(?:[·-])\s*/);

    return {
      date: dateMatch ? dateMatch[1] : '',
      href: toRouteHref(markdownPath),
      markdownPath: markdownPath,
      summary: dateMatch ? dateMatch[1] : '',
      title: link.textContent.trim()
    };
  }

  function renderFeaturedCards(list, latestArticles) {
    if (latestArticles && latestArticles.length) {
      renderLatestFeaturedCards(list, latestArticles);
      return;
    }

    Array.from(list.children).forEach(function (item) {
      if (item.tagName !== 'LI' || item.classList.contains('home-reading-item')) {
        return;
      }

      var link = item.querySelector('a[href]');

      if (!link) {
        return;
      }

      var markdownPath = toMarkdownPath(link.getAttribute('href') || '');

      if (!markdownPath || !isArticleMarkdown(markdownPath)) {
        return;
      }

      var summaryNode = Array.from(item.querySelectorAll('p')).find(function (paragraph) {
        return !paragraph.querySelector('a[href]');
      });

      renderFeaturedCard({
        href: toRouteHref(markdownPath),
        item: item,
        markdownPath: markdownPath,
        summary: summaryNode ? summaryNode.textContent.trim() : '',
        title: link.textContent.trim()
      });
    });
  }

  function renderLatestFeaturedCards(list, articles) {
    var key = articles.map(function (article) {
      return article.date + ':' + article.markdownPath;
    }).join('|');

    if (list.getAttribute('data-home-latest-key') === key) {
      return;
    }

    list.setAttribute('data-home-latest-key', key);
    list.textContent = '';

    articles.forEach(function (article) {
      var item = document.createElement('li');

      list.appendChild(item);
      renderFeaturedCard({
        date: article.date,
        href: article.href,
        item: item,
        markdownPath: article.markdownPath,
        summary: article.summary,
        title: article.title
      });
    });
  }

  function renderFeaturedCard(article) {
    var item = article.item;
    var card = document.createElement('a');
    var media = document.createElement('span');
    var body = document.createElement('span');
    var title = document.createElement('span');
    var summary = document.createElement('span');

    item.className = 'home-reading-item';
    card.className = 'home-reading-card';
    card.href = article.href;
    media.className = 'home-reading-card-media is-loading';
    media.innerHTML = '<span>AI</span>';
    body.className = 'home-reading-card-body';
    title.className = 'home-reading-card-title';
    summary.className = 'home-reading-card-summary';
    title.textContent = article.title;
    summary.textContent = article.summary;

    body.appendChild(title);
    body.appendChild(summary);
    card.appendChild(media);
    card.appendChild(body);
    item.textContent = '';
    item.appendChild(card);

    getCover(article.markdownPath).then(function (cover) {
      media.classList.remove('is-loading');

      var image = document.createElement('img');
      image.alt = article.title;
      image.loading = 'lazy';
      image.src = cover || createGeneratedCover(article.title);
      media.textContent = '';
      media.appendChild(image);
    });
  }

  function renderFeatureCards(list) {
    Array.from(list.children).forEach(function (item) {
      if (item.tagName !== 'LI' || item.classList.contains('home-feature-item')) {
        return;
      }

      var link = item.querySelector('a[href]');

      if (!link) {
        return;
      }

      var summaryNode = Array.from(item.querySelectorAll('p')).find(function (paragraph) {
        return !paragraph.querySelector('a[href]');
      });
      var href = link.getAttribute('href') || '#/';
      var title = link.textContent.trim();
      var summary = summaryNode ? summaryNode.textContent.trim() : '';
      var card = document.createElement('a');
      var media = document.createElement('span');
      var image = document.createElement('img');
      var body = document.createElement('span');
      var titleNode = document.createElement('span');
      var summaryNodeNew = document.createElement('span');

      item.className = 'home-feature-item';
      card.className = 'home-feature-card';
      card.href = href;
      media.className = 'home-feature-card-media';
      image.alt = title;
      image.loading = 'lazy';
      image.src = createGeneratedCover(title, summary || 'cxuan-ai-labs');
      body.className = 'home-feature-card-body';
      titleNode.className = 'home-feature-card-title';
      summaryNodeNew.className = 'home-feature-card-summary';
      titleNode.textContent = title;
      summaryNodeNew.textContent = summary;

      media.appendChild(image);
      body.appendChild(titleNode);
      body.appendChild(summaryNodeNew);
      card.appendChild(media);
      card.appendChild(body);
      item.textContent = '';
      item.appendChild(card);
    });
  }

  function toArticleItem(listItem) {
    var link = listItem.querySelector('a[href]');

    if (!link) {
      return null;
    }

    var href = link.getAttribute('href') || '';
    var markdownPath = toMarkdownPath(href);

    if (!markdownPath || !isArticleMarkdown(markdownPath)) {
      return null;
    }

    var rawText = listItem.textContent.replace(/\s+/g, ' ').trim();
    var dateMatch = rawText.match(/^(\d{4}-\d{2}-\d{2})\s*-\s*/);

    return {
      date: dateMatch ? dateMatch[1] : '',
      href: toRouteHref(markdownPath),
      item: listItem,
      markdownPath: markdownPath,
      title: link.textContent.trim()
    };
  }

  function renderCard(article) {
    var item = article.item;

    if (item.classList.contains('article-card-item')) {
      return;
    }

    var card = document.createElement('a');
    var media = document.createElement('span');
    var body = document.createElement('span');
    var date = document.createElement('span');
    var title = document.createElement('span');

    item.className = 'article-card-item';
    card.className = 'article-card';
    card.href = article.href;
    media.className = 'article-card-media is-loading';
    media.innerHTML = '<span>AI</span>';
    body.className = 'article-card-body';
    date.className = 'article-card-date';
    title.className = 'article-card-title';
    date.textContent = article.date || 'AI Article';
    title.textContent = article.title;

    body.appendChild(date);
    body.appendChild(title);
    card.appendChild(media);
    card.appendChild(body);
    item.textContent = '';
    item.appendChild(card);

    getCover(article.markdownPath).then(function (cover) {
      media.classList.remove('is-loading');

      var image = document.createElement('img');
      image.alt = article.title;
      image.loading = 'lazy';
      image.src = cover || createGeneratedCover(article.title);
      media.textContent = '';
      media.appendChild(image);
    });
  }

  function getCover(markdownPath) {
    if (coverCache.has(markdownPath)) {
      return coverCache.get(markdownPath);
    }

    var request = fetch(markdownPath + '?v=20260531-card-cover', {
      cache: 'force-cache'
    })
      .then(function (response) {
        if (!response.ok) {
          return '';
        }

        return response.text();
      })
      .then(function (markdown) {
        return extractFirstImage(markdown, markdownPath);
      })
      .catch(function () {
        return '';
      });

    coverCache.set(markdownPath, request);
    return request;
  }

  function extractFirstImage(markdown, markdownPath) {
    var imagePattern = /!\[[^\]]*]\(([^)\s]+)(?:\s+["'][^"']*["'])?\)|<img[^>]+src=["']([^"']+)["'][^>]*>/ig;
    var imageMatch = imagePattern.exec(markdown);
    var src = imageMatch && (imageMatch[1] || imageMatch[2]);

    if (src) {
      return resolveImageSource(src, markdownPath);
    }

    return '';
  }

  function getCurrentRoute() {
    return (window.location.hash || '#/').replace(/^#\/?/, '').split('?')[0];
  }

  function getCurrentMarkdownPath(route) {
    var path = (route || '').replace(/^\/+/, '');

    if (!path || path === 'README' || /\/README$/.test(path)) {
      return '';
    }

    if (!/\.md$/i.test(path)) {
      path += '.md';
    }

    return path;
  }

  function isArticleIndexRoute(route) {
    return (
      route === 'ai-articles' ||
      route === 'ai-articles/' ||
      route === 'ai-articles/README' ||
      /^ai-articles\/[^/]+\/README$/.test(route) ||
      route === 'en/ai-articles' ||
      route === 'en/ai-articles/' ||
      route === 'en/ai-articles/README' ||
      /^en\/ai-articles\/[^/]+\/README$/.test(route)
    );
  }

  function isHomeRoute(route) {
    return route === '' || route === '/' || route === 'README' || route === 'README.zh-CN';
  }

  function isArticleMarkdown(path) {
    return (
      (
        /^ai-articles\/[^/]+\/.+\.md$/.test(path) ||
        /^en\/ai-articles\/[^/]+\/.+\.md$/.test(path)
      ) &&
      !/\/README\.md$/.test(path)
    );
  }

  function toMarkdownPath(href) {
    var route = '';

    if (href.indexOf('#/') === 0) {
      route = href.slice(2);
    } else if (href.indexOf('#/') > -1) {
      route = href.split('#/')[1];
    } else if (/\.md(?:$|[?#])/.test(href)) {
      route = resolveRelativeMarkdownPath(href);
    }

    route = route.split('?')[0].split('#')[0].replace(/^\/+/, '');

    if (!route) {
      return '';
    }

    if (!/\.md$/i.test(route)) {
      route += '.md';
    }

    return route;
  }

  function toRouteHref(markdownPath) {
    return '#/' + markdownPath.replace(/\.md$/i, '').replace(/^\/+/, '');
  }

  function normalizeMarkdownPath(markdownPath) {
    var normalized = (markdownPath || '').replace(/^\/+/, '');

    try {
      return decodeURIComponent(normalized);
    } catch (error) {
      return normalized;
    }
  }

  function resolveRelativeMarkdownPath(href) {
    var base = getCurrentRoute();

    if (!base || base === 'README') {
      base = '';
    } else if (/\/README$/.test(base)) {
      base = base.replace(/README$/, '');
    } else {
      base = base.replace(/[^/]+$/, '');
    }

    var rootPath = getSiteRootPath();
    var url = new URL(href, window.location.origin + rootPath + base);
    var path = url.pathname;

    if (path.indexOf(rootPath) === 0) {
      path = path.slice(rootPath.length);
    }

    return path.replace(/^\/+/, '');
  }

  function resolveImageSource(src, markdownPath) {
    var trimmed = (src || '').trim();

    if (/^(?:https?:)?\/\//i.test(trimmed) || /^(?:data|blob):/i.test(trimmed) || trimmed.charAt(0) === '/') {
      return trimmed;
    }

    var rootPath = getSiteRootPath();
    var articleDirectory = markdownPath.replace(/[^/]+$/, '');

    return new URL(trimmed, window.location.origin + rootPath + articleDirectory).href;
  }

  function getSiteRootPath() {
    var path = window.location.pathname;

    return path.charAt(path.length - 1) === '/' ? path : path.replace(/[^/]*$/, '');
  }

  function createGeneratedCover(title, caption) {
    var safeTitle = escapeXml(title || 'AI Article');
    var safeCaption = escapeXml(caption || 'AI notes · tools · workflow');
    var svg = [
      '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540">',
      '<rect width="960" height="540" fill="#effaf6"/>',
      '<rect x="44" y="44" width="872" height="452" rx="24" fill="#ffffff" stroke="#bfe8dc" stroke-width="2"/>',
      '<path d="M80 388H880" stroke="#00b38a" stroke-width="8" stroke-linecap="round"/>',
      '<text x="80" y="148" fill="#008f70" font-family="Arial, sans-serif" font-size="34" font-weight="700">cxuan-ai-labs</text>',
      '<foreignObject x="80" y="194" width="800" height="150">',
      '<div xmlns="http://www.w3.org/1999/xhtml" style="font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Arial,sans-serif;font-size:44px;font-weight:800;line-height:1.28;color:#303c39;">',
      safeTitle,
      '</div>',
      '</foreignObject>',
      '<foreignObject x="80" y="426" width="800" height="52">',
      '<div xmlns="http://www.w3.org/1999/xhtml" style="font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Arial,sans-serif;font-size:22px;font-weight:600;line-height:1.35;color:#7b8a86;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">',
      safeCaption,
      '</div>',
      '</foreignObject>',
      '</svg>'
    ].join('');

    return 'data:image/svg+xml;charset=UTF-8,' + encodeURIComponent(svg);
  }

  function escapeXml(text) {
    return String(text).replace(/[&<>"']/g, function (char) {
      return {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;'
      }[char];
    });
  }
}());
