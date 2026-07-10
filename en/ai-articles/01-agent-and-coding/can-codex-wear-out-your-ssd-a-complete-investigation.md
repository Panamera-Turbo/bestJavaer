# Can Codex Wear Out Your SSD? A Complete Investigation

[English](./can-codex-wear-out-your-ssd-a-complete-investigation.md) | [Chinese Original](../../../ai-articles/01-agent-and-coding/Codex%20%E4%BC%9A%E6%8A%8A%E7%A3%81%E7%9B%98%E7%BB%99%E7%83%A7%E4%BA%86%EF%BC%9F%E5%AE%8C%E6%95%B4%E5%A4%8D%E7%9B%98%E6%9D%A5%E4%BA%86%EF%BC%81.md)

> English edition based on the Chinese original.

> Date: 2026-06-24

A worrying claim has been circulating among heavy Codex users:

Long Codex sessions, especially long-running Agent work, may continuously write to `~/.codex/logs_2.sqlite`. The database may appear to be only a few hundred megabytes while the actual volume written to the SSD is much higher.

I thought that sounded exaggerated until I checked my own machine.

```text
~/.codex/logs_2.sqlite      about 823 MB
~/.codex/logs_2.sqlite-wal  about 38 MB
Rows retained in logs       61,418
Estimated TRACE content     70.6 MiB
MAX(id) increase in 15 sec  10,364
Change in retained rows     0
```

<img src="https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/e6c35348ba0317c184c5684da5a995cee23fa0cf.png" alt="Read-only sample from the local Codex logs_2.sqlite database" style="zoom:50%;" />

*Prepared from a read-only sample of my local `~/.codex/logs_2.sqlite`.*

Look at the last two lines.

The number of retained rows did not change, yet `MAX(id)` increased by more than ten thousand in 15 seconds.

Codex was constantly writing new logs while replacing old ones. The visible database did not grow much, but the disk still handled repeated writes.

Real-time logging is normal. Keeping a recent window of logs is normal too.

The problem is the volume of small TRACE events written into local SQLite and the continuous removal of old rows. The table may keep only tens of thousands of records while storage activity continues underneath.

The important signal is not a rapidly increasing row count or a visibly exploding database file. **The file can remain nearly the same size while total SSD writes rise sharply.**

## How the Issue Developed

This was not one person's mistaken impression.

On April 10, 2026, a user opened issue `#17320` in the OpenAI Codex repository. They observed Codex continuously writing to `~/.codex/logs_2.sqlite-wal` during streamed output, at rates measured in megabytes per second.

![Codex issue report](https://cdn.jsdelivr.net/gh/doggaifan/picbed@main/image-20260623132408985.png)

Similar reports became more common during May and June.

Some users saw WAL files grow for long periods. Deleting them did not release the space because an older Codex process still held the deleted file handle.

Other users watched `logs_2.sqlite` and its WAL grow quickly after only a few minutes of ordinary Codex Desktop use, while the interface became slower.

<img src="https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/663ef07fe7cc0ada871b9924c422cdfa51d38fcc.png" alt="Redrawn diagram based on a community Codex local state report" style="zoom:50%;" />

*Prepared from a community screenshot of Codex local state.*

Issue `#28224` brought the problem into wider view.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed@main/image-20260623132541418.png" alt="Codex issue 28224" style="zoom:50%;" />

On June 14, 2026, a user estimated SSD writes from their own machine. During 21 days of ordinary operation, the primary SSD had received about 37 TB of writes. At that rate, the annualized total approached 640 TB.

<img src="https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/5fc40b1757b6c52f3a72bd64f9c4ed8947c88cd7.png" alt="Redrawn community example where logs_2.sqlite reached 38.2 GB" style="zoom:50%;" />

*Prepared from a file-size screenshot shared in an X discussion.*

That number represents one machine. It does not mean every user will see the same volume.

But the report established a real risk:

**Under some usage patterns, Codex diagnostic logging can keep writing to disk and push SSD write volume to an extreme level.**

The highest-risk users are those who:

- Leave Codex Desktop running for long periods.
- Use `codex resume` frequently.
- Run long streamed tasks over WebSocket and similar connections.
- Keep several Codex, TUI, or Desktop processes running at once.
- Use a small SSD, an SD card, or lower-endurance storage.

If you only use Codex occasionally, the risk is lower.

If Codex is a constant working companion and you run it continuously for hours or days, especially with long-running goals or plan mode, it is worth checking.

## What the Problem Looks Like

The issue centers on three files:

```text
~/.codex/logs_2.sqlite
~/.codex/logs_2.sqlite-wal
~/.codex/logs_2.sqlite-shm
```

They make up Codex's local SQLite logging database.

When SQLite uses WAL mode, writes usually land in the `-wal` file first and are later merged into the main database through a checkpoint.

WAL is normal. Many applications use it.

The problem is the amount and type of data Codex recorded.

First, successful streaming events were logged.

A normal piece of model output, a tool-status refresh, or a successfully parsed response could all become log entries. A long task then produced writes throughout every call.

Second, many TRACE logs were persisted locally.

TRACE is fine for temporary debugging. Persisting high-volume TRACE data to disk over time, especially through SQLite, can create a large write load.

Third, old entries were continuously replaced.

Users saw only tens of thousands of rows and assumed the database was stable.

The actual pattern could be constant insertion followed by constant deletion. The visible row count remains unchanged while the disk continues to receive writes.

That is exactly what my sample showed: `MAX(id)` rose by 10,364 in 15 seconds while the total row count did not change.

<img src="https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/db21df4351e12ba2533950e5f37bad0beac5ee16.png" alt="Why the SSD can keep receiving writes while the visible log row count stays flat" style="zoom:50%;" />

*Prepared from OpenAI Codex issues, pull requests, and my local sample.*

## How OpenAI Responded

There is an important update: OpenAI has fixed the main source of excessive writes described here.

I checked the official repository on June 23, 2026. On June 22, the Codex repository merged two relevant pull requests from collaborator `jif-oai`.

PR `#29432` stopped logging every Responses WebSocket event.

![PR 29432](https://cdn.jsdelivr.net/gh/doggaifan/picbed@main/image-20260623133530667.png)

PR `#29457` filtered high-noise sources from the local log database.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed@main/image-20260623133633698.png" alt="PR 29457" style="zoom:50%;" />

In other words, high-frequency logs with little everyday diagnostic value would no longer be written to local SQLite by default.

After those fixes merged, issue `#28224` closed on June 22, 2026. The GitHub Releases page also showed two alpha prerelease tags that day: `rust-v0.142.0-alpha.11` and `rust-v0.142.0-alpha.12`.

![Codex alpha releases](https://cdn.jsdelivr.net/gh/doggaifan/picbed@main/image-20260623134839585.png)

The release page did not include a detailed changelog, so those tags should only be described as prereleases that appeared after the fixes merged, not as an official release announcement for the fix.

When I checked, related issues `#17320`, `#22444`, and `#24275` were still open. They also cover WAL files held by old processes, deleted files that do not release space, and Desktop log-database growth.

The accurate summary is:

**OpenAI has merged fixes for the main high-frequency TRACE write problem. WAL lifecycle, old-process file handles, and health warnings still need observation.**

## What You Should Do Now

The first step for ordinary users is to update Codex.

Use a version that includes fixes merged after June 22, 2026. Version numbers differ across installation channels, so check the method you used to install Codex.

Then inspect the files on your machine.

### Short Version: Give This Prompt to an AI

If you do not want to run each command manually, use this read-only diagnostic prompt:

````text
Help me perform a read-only investigation of whether ~/.codex/logs_2.sqlite
is still receiving high-frequency writes from TRACE logs or streaming events.

Constraints:
1. Read-only diagnosis only.
2. Do not delete files, run VACUUM, checkpoint or truncate the WAL, change the
   schema, create a trigger, kill a process, upgrade Codex, or reinstall it.
3. Open SQLite only through this read-only URI:
   db="file:$HOME/.codex/logs_2.sqlite?mode=ro".
4. If sqlite3, lsof, or the database file is missing, say so. Do not guess.
5. Finish with: whether the machine appears affected, the evidence, a risk
   level, and suggested next steps.

Run the following checks in order and explain the results.

First, confirm file sizes:

```bash
du -h \
  ~/.codex/logs_2.sqlite \
  ~/.codex/logs_2.sqlite-wal \
  ~/.codex/logs_2.sqlite-shm 2>/dev/null

ls -lh ~/.codex/logs_2.sqlite* 2>/dev/null
```

Second, inspect the SQLite schema and log distribution in read-only mode:

```bash
db="file:$HOME/.codex/logs_2.sqlite?mode=ro"

sqlite3 "$db" "PRAGMA table_info(logs);"

sqlite3 "$db" "
PRAGMA journal_mode;
PRAGMA wal_autocheckpoint;
SELECT COUNT(*) AS rows, MIN(id), MAX(id) FROM logs;
SELECT level, COUNT(*) AS rows, ROUND(SUM(estimated_bytes)/1024.0/1024.0, 1) AS mib
FROM logs
GROUP BY level
ORDER BY SUM(estimated_bytes) DESC;
"
```

Third, take a 15-second sample:

```bash
db="file:$HOME/.codex/logs_2.sqlite?mode=ro"
before_id=$(sqlite3 "$db" "SELECT COALESCE(MAX(id),0) FROM logs;")
before_count=$(sqlite3 "$db" "SELECT COUNT(*) FROM logs;")
sleep 15
after_id=$(sqlite3 "$db" "SELECT COALESCE(MAX(id),0) FROM logs;")
after_count=$(sqlite3 "$db" "SELECT COUNT(*) FROM logs;")
echo "id_delta=$((after_id-before_id))"
echo "count_delta=$((after_count-before_count))"
```

Fourth, check whether Codex processes hold the database or WAL:

```bash
lsof -nP \
  ~/.codex/logs_2.sqlite \
  ~/.codex/logs_2.sqlite-wal \
  ~/.codex/logs_2.sqlite-shm 2>/dev/null
```

Interpretation:
- A high id_delta with a small or zero count_delta suggests continuous inserts
  followed by pruning of old logs.
- A continuously growing logs_2.sqlite-wal, or an old process holding a deleted
  WAL, deserves a warning.
- A low id_delta, a stable WAL, and only the current Codex process opening the
  files suggests normal operation.
- Do not apply a fix. List options and risks, then wait for my confirmation.
````

That prompt detected the problem on my own machine.

<img src="https://cdn.jsdelivr.net/gh/doggaifan/picbed@main/image-20260623142826935.png" alt="Read-only Codex logging diagnosis" style="zoom:50%;" />

Perhaps that proves I really am a heavy Codex user.

### Manual Version

The manual check begins with file size:

```bash
du -h \
  ~/.codex/logs_2.sqlite \
  ~/.codex/logs_2.sqlite-wal \
  ~/.codex/logs_2.sqlite-shm 2>/dev/null

ls -lh ~/.codex/logs_2.sqlite* 2>/dev/null
```

Then inspect SQLite in read-only mode:

```bash
db="file:$HOME/.codex/logs_2.sqlite?mode=ro"
sqlite3 "$db" "
PRAGMA journal_mode;
PRAGMA wal_autocheckpoint;
SELECT COUNT(*) AS rows, MIN(id), MAX(id) FROM logs;
SELECT level, COUNT(*) AS rows, ROUND(SUM(estimated_bytes)/1024.0/1024.0, 1) AS mib
FROM logs
GROUP BY level
ORDER BY SUM(estimated_bytes) DESC;
"
```

The `mode=ro` parameter opens the database read-only. A diagnostic check should avoid modifying the database it is measuring.

Take a short sample:

```bash
db="file:$HOME/.codex/logs_2.sqlite?mode=ro"
before_id=$(sqlite3 "$db" "SELECT COALESCE(MAX(id),0) FROM logs;")
before_count=$(sqlite3 "$db" "SELECT COUNT(*) FROM logs;")
sleep 15
after_id=$(sqlite3 "$db" "SELECT COALESCE(MAX(id),0) FROM logs;")
after_count=$(sqlite3 "$db" "SELECT COUNT(*) FROM logs;")
echo "id_delta=$((after_id-before_id))"
echo "count_delta=$((after_count-before_count))"
```

If `id_delta` stays low after the update and the WAL no longer grows continuously, leave the database alone.

Manual remediation only makes sense if you are still on an old version or you confirm high-frequency writes after updating.

Before changing anything, check whether a process holds the files:

```bash
lsof -nP ~/.codex/logs_2.sqlite ~/.codex/logs_2.sqlite-wal ~/.codex/logs_2.sqlite-shm 2>/dev/null
```

If an old Codex process is present, close it first. A process holding a deleted WAL can prevent space from being released even after the file disappears from the directory.

Then create a backup:

```bash
backup_dir="$HOME/.codex/logs_backup_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$backup_dir"
find "$HOME/.codex" -maxdepth 1 -name 'logs_2.sqlite*' -exec cp -p {} "$backup_dir"/ \;
```

<img src="https://cdn.jsdelivr.net/gh/crisxuan/searchnews-assets@main/281e3f7705a4e8dd2bb05cfb01349ea3479de500.jpg" alt="Close processes, back up files, stop writes, truncate the WAL, and monitor growth" style="zoom:50%;" />

*Prepared from community workarounds and SQLite cleanup guidance.*

One community workaround for immediate damage control is a SQLite trigger that ignores new inserts into the `logs` table:

```bash
sqlite3 ~/.codex/logs_2.sqlite "
CREATE TRIGGER IF NOT EXISTS block_log_inserts
BEFORE INSERT ON logs
BEGIN
  SELECT RAISE(IGNORE);
END;
PRAGMA wal_checkpoint(TRUNCATE);
"
```

To remove it:

```bash
sqlite3 ~/.codex/logs_2.sqlite "
DROP TRIGGER IF EXISTS block_log_inserts;
"
```

This can stop the writes temporarily, but it also makes future Codex diagnostic logs incomplete. If you later need to report a problem to OpenAI, important evidence may be missing.

My recommendation is simple:

Update first. Check again. If high-frequency writes continue, make a backup before applying a temporary block.

## My View

As AI coding tools become persistent system services, using the Agent is only part of the job. Heavy users also need to inspect and maintain the system around it.

These tools run local servers, keep WebSocket connections, record sessions, write runtime data, and manage background tasks.

Combined, those capabilities mean one logging mistake can become a system-level resource problem.

We used to worry about AI writing buggy code. Now we also have to check whether the AI tool itself is writing the disk too aggressively.

This does not mean people should stop using Codex. I still use it.

But heavy users should build a habit: **once an AI Agent becomes persistent, treat it as AI infrastructure.**

Inspect it periodically.

For an occasional user, this may be a few hundred megabytes of low-value logs.

For a heavy user, it may affect SSD endurance and system stability.

OpenAI has fixed the main bug, but it is still worth remaining alert.

That is the lesson from this incident.

---

## Sources

- [OpenAI Codex issue #17320](https://github.com/openai/codex/issues/17320)
- [OpenAI Codex issue #22444](https://github.com/openai/codex/issues/22444)
- [OpenAI Codex issue #24275](https://github.com/openai/codex/issues/24275)
- [OpenAI Codex issue #28224](https://github.com/openai/codex/issues/28224)
- [OpenAI Codex PR #29432](https://github.com/openai/codex/pull/29432)
- [OpenAI Codex PR #29457](https://github.com/openai/codex/pull/29457)
- [OpenAI Codex release 0.142.0-alpha.11](https://github.com/openai/codex/releases/tag/rust-v0.142.0-alpha.11)
- [OpenAI Codex release 0.142.0-alpha.12](https://github.com/openai/codex/releases/tag/rust-v0.142.0-alpha.12)
- [SQLite documentation: Write-Ahead Logging](https://sqlite.org/wal.html)
- [Tencent Cloud Developer Community: Codex 5.5 feels weaker? Check these local files first](https://developer.cloud.tencent.com/article/2676528)
- [SegmentFault: Safely cleaning local Codex conversation history](https://segmentfault.com/a/1190000047816752)
- [X discussion about Codex streaming and local log writes](https://x.com/bdsqlsz/status/2067964486615810369)
