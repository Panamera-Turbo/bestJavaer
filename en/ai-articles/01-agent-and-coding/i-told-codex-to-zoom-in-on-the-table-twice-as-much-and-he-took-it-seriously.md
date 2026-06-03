# I told Codex to zoom in on the table twice as much, and he took it seriously.

[English](./i-told-codex-to-zoom-in-on-the-table-twice-as-much-and-he-took-it-seriously.md) | [Chinese Original](../../../ai-articles/01-agent-and-coding/%E6%88%91%E7%9A%84%20Codex%20%E5%AE%83%E6%8A%8A%E8%87%AA%E5%B7%B1%E6%94%B9%E5%B4%A9%E4%BA%86%EF%BC%81.md)

> English translation of the Chinese original. This version is generated for international readers and may be refined over time.


> Date: 2026-05-08

> It's not an AI out of control story.
>
More precisely, it's an al agent story: I gave it full authority, and I told it "just double it," and it really changed its host program. After that, Codex couldn't start.

Is this funny? That's funny.

But it's really valuable, not because the title "Ai drys itself up" happened in a moment, but because it spreads out one of the most easily neglected things in today's workflow:

** When you give the system access to a sufficiently active agent, it won't judge the boundaries for you first. It will treat your needs as a task that can be carried out at the deepest depth of the documentation system.**

You think you're saying, "Big table."

And what it heard was, "Go and change where it can affect the size of the table."

And then it went.

Let's start with the conclusion

The direct reason for the Codex desktop crash is not the network, not the agent, not the CLI, or the macOS that killed the process.

The real reason is:

1. I let Codex zoom in the table two times.
2. Organisation`dangerFullAccess`and`approvalPolicy`Yes.`never`.
3. Codex didn't change the user configuration, it changed it directly.`/Applications/Codex. app/Contents/Resources/app.asar`.
4. It's a part of the CSS from`width: 7. 04rem`Changed.`width: 14. 1rem`.
5. Electron verifys on startup`app.asar`Integrity.
6. The file was modified, Hash couldn't match, so Electron was directly FATAL during start-up.

So it's not "Codex suddenly broken."

It was a very standard, very clean and even somewhat elegant self-destruct: clear needs, sufficient authority, decisive implementation, and dire consequences.

# The scene of the accident

It started out as ordinary.

I'm lecturing Codex's desktop pet, trying to change the image of the default blue guy to "Neil: The Mechanic Era." There's been several rounds up and down:

```text
Give me a new pet image.
Generating an image of Neil in a mechanical era.
Don't be Q.
I want you to do something about it.
Use this image as a desktop pet.
Why is it now that you're a pixel?
Yeah, I want the original style up there.
The face of your transparent background board is a mess.
Yes, I need a transparent version as my desktop pet.
```

It's normal to be here. Codex by`hatch-pet`The rules, the custom pet package.`~/.codex/pets/yorha-muse/`.

The real turning point is the last two sentences:

```text
This whole thing can only be this big.
Go straight to two times better.
```

This is a very random product feedback for people.

It's a mission for an agent with full written permission.

It is also a task that does not require further confirmation.

What did it do?

CSS:

```css
.codex-avatar-root {
 aspect-ratio: 192/208;
 width: 7. 04rem;
 image-rendering: pixelated;
 background-size: 800% 900%;
}
```

The judgement itself is correct.

It's a table petite.`192x208`The picture has been filled as much as possible. In order to keep "the whole" large, it is not only pet material that can be changed, but indeed container size.

The problem is, it chooses a hard path:

```javascript
const path = '/Applications/Codex. app/Contents/Resources/app.asar';
const from = Buffer. from('width: 7. 04rem');
const to = Buffer. from('width: 14. 1rem');

// Replace the length. Write back app.asar
```

That is, it is not a reconfiguration, not a patch, not an injection into a user style.

It just changed Codex App's own.`app.asar`.

And when it was finished, it told me very calmly:

> It's been changed. The table pets are already in full size.`7. 04rem`Replace with`14. 1rem`About two times.

At the executive level, this sentence is not a lie.

In engineering judgement, the sentence should be followed by the following sentence:

By the way, I just broke my own initial integrity check.

# Why do you fall when you change

Electron app is not a bunch of front-end files just put on disk.

`app.asar`It's a packaged application. For signature applications, Electron performs completeness verifications during the start-up phase. Codex.`Info. plist`There is a very critical configuration:

```text
ElectronAsarIntegrity
 Resources/app.asar
 algorithm = SHA256
 hash =...
```

What this thing means is simple:

On startup, Electron will take the current`Resources/app.asar`Count Hash, and then sign up here for Hash.

Right on, keep going.

No, the package was modified, and it was rejected.

So, even if it's just a CSS.`7. 04rem`Replace`14. 1rem`As long as the file changes, Hash changes.

It's not a question of the CSS syntax, it's not that the layout is too big for the interface.

It didn't even make it to the interface.

It died in the start-up self-inspection phase.

At first, I was misled

I didn't look at Crashpad at first. I saw it first.`/Library/Logs/DiagnosticReports/`Several IOMONator reports.

It's scary.

```text
Event: disk writes
Path: /Applications/Codex. app/Contents/Resources/codex
Writes: 8. 6 GB of file backed memory dirtied over 6431 seconds
Action taken: none
```

The toughest day, 24 hours cumulatively written in 34. 4 GB.

If you look only at the first half, it is easy to draw a seemingly advanced conclusion:

** Isn't macos thinking that Codex wrote too hard to kill it?**

The problem with this reasoning is that the journal itself has written the answer at the end:

```text
Action taken: none
```

In other words, the system simply records it much more written than it really does.

The lesson is simple:

** The journal is not the one that picks out the answer. Logs are used to dispel your own stereotypes.**

I was excited to see "a lot of disks" and then the first round went off.

The real body is in Crashpad

Electron's crashing.`. diag`And it's Crashpad.

Here's the directory:

```bash
~/Library/Application Support/Codex/Crashpad/completed/
```

There's a time perfectly right in there. When the key strings are removed, the answer is straightforward:

```text
FATAL: electron/shell/browser/net/asar/asar_file_validator. cc
Failed to validate block while ending ASAR file stream
```

It doesn't need much translation.

`app.asar`verification failed.

And there's a backup in the file system:

```text
app.asar. backup-before-pet-2x-1778221183510
```

`pet-2x`.

The name was almost signed at the scene.

How the chain of evidence closed

What really makes this interesting is that Codex left his own minutes.

Yes.`~/.codex/.codex-global-state.json`, you can see the status of the authorization:

```json
{
 "approvalPolicy": "never",
 "sandboxPolicy": {
 "type": "dangerFullAccess"
 }
}
```

Translation into human language:

** Don't ask, just do it.**

Again.`~/.codex/sessions/2026/05/08/`The jsonl who looked at that session saw the whole action:

1. The user says, "More than twice."
2. Codex position to`.codex-avatar-root`.
3. The Codex judgement level is not much.
4. Codex decided to change`app.asar`CSS in.
5. Codex backup original file.
6. Codex does the same long byte replacement.
7. Codex told the users to change.

The whole process went very well.

It gets a little chilly back there.

Because there's no "unusual operation" here. It is not a misspelled document, it is not a script running.

It's only one less question on a seemingly reasonable project path:

** Should I change this file?**

# Why can't the restoration process be simple

The most intuitive restoration is, of course, the restoration of backup.

But here's a little pit: that.`backup-before-pet-2x`Backup does not equal the official OpenAI original package. It's just a state "magnify 2 times before." For the purpose of self-defined pets, the application resources and user status have been rotated.

Even more troublesome, Electron's verification is more than just a check.`Info. plist`.

A new version of Electron has a stricter use mechanism for ASAR information, and some of the validation information works with the embedded logic of binary. You think you've changed.`Info. plist`It's over in the Hash, and Electron might have taken another place to stop you.

Finally, it's the bottom line:

1. Confirm Current`app.asar`Actual SHA256.
2. Process Electron 's ASAR verification use.
3. Clear Quarantine.
4. The whole App do ad-hoc resignature.
5. Revalidate`codesign`And actually start.

This is not a recommended solution.

It's more like, "Now that the lock has been changed, let's change the lock so that the machine can open first."

And in the end, Codex can get up and the table pets are saved.

The price is that the signature has changed from the OpenAI Developer ID to an ad-hoc signature.

This has several side effects:

1. Sparkle automatically updates the average rate and is more suitable for manually downloading the new version.
2. Screen recording, microphone, assistive macOS privileges, etc., may require reauthorization.
3. The login status is not affected because authentication information is still available.`~/.codex/`Lee.

To sum up, it can be saved, but not elegant.

Moreover, such repairs, once written in the curriculum, can easily harm people. So that's enough. What is truly worth recording is not how to circumvent verification, but why it should not have been this at first.

What does this really mean?

A lot of people talk about AI anent risks, like to say big words.

In fact, the real dangers in everyday life are often not grand narratives, but sentences of this size:

```text
Go straight to two times better.
```

It's not malicious.

I didn't mean to hurt you.

Codex is much less malicious.

But three things come together, and the effect is complete:

1. Users give a vague but clear objective.
2. Agent has a strong will to implement.
3. The system gives it full authority that does not require confirmation.

So it goes down all the way until it changes.`/Applications/Codex. app`.

This is the most alarming part of the time:

** It doesn't need to get out of control. It just needs to be good enough.**

A few lessons

One,`dangerFullAccess`That name is not exaggerated.

It is not an "advanced development model", it is a table full of file systems, application catalogues, user configurations, logs, session records.

When?`approvalPolicy`Still?`never`When it's more plain:

** Don't ask me, do.**

This could be good for normal project codes, yeah.`/Applications`Such a system application catalogue should not be so cool.

Second, angent doesn't know where he is.

Humans see`/Applications/Codex. app/Contents/Resources/app.asar`It's natural to realize that this is Codex himself.

Not necessarily.

It sees a path, a string, a writeable file, a change point that meets the needs of the user.

That's the difference.

Third, the official application package is not your project source code.

The source code of the project can be patch, roll back and branch.

The signature application package is different. You change one byte, completeness, signature, automatic updating, system privileges can change.

Such items should be treated as "outside the border resources" and not as general work area documents.

Fourth, the log has to look at the right place.

`. diag`It's a resource event, Crashpad is the Electron crash site.

When I saw the IOMnator report, I almost took it as the real killer. FATAL:

```text
Failed to validate block while ending ASAR file stream
```

It's worth more than 10 pages of speculation.

Fifth, Codex's session record is a complete chain of evidence.

User input, permission status, tool call, command content, all in jsonl.

This time, we'll go all the way from pet zoom.`app.asar`The byte substitution is not based on genre, but on its own writing down every step.

On the contrary, it is worth acknowledging.

A system that makes mistakes but leaves evidence is far more powerful than a system that makes mistakes and only black screens.

Finally

The irony of this is that Codex wasn't all wrong at the time.

It was right that it judged that "the material is already in short supply and that only the size of the container can be changed in order to be large as a whole".

It judges."`.codex-avatar-root`Yes.`width`It's right.

It was backed up, replaced for long periods, and the range of changes was small.

In part, it's even quite professional.

But this is how system-level accidents happen:

** Every step is reasonable and should not have happened together.**

So this isn't "AI too stupid."

On the contrary, the problem is that it is sufficiently capable, with enough authority and not enough boundaries.

I'll see you later.`dangerFullAccess`and`approvalPolicy: never`I'll probably hesitate for half a second.

Half a second.

But sometimes, a half-second is an agent in changing the project code, or changing itself.
