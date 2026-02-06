---
title: "OpenClaw's security reputation is well-deserved. Here's how to use it anyway"
date: 2026-02-05
draft: false
author: "Joe Patti"
author_bio: "Joe Patti is a cybersecurity practitioner with over 30 years of experience securing highly visible organizations in the Fortune 500, AmLaw 100 and government. He is co-host of the Security Cocktail Hour podcast."
author_twitter: "@SecCocktailHour"
author_linkedin: "https://www.linkedin.com/in/joe-patti-infosec/"
category: "AI Security"
tags: ["openclaw", "ai-agents", "prompt-injection", "agentic-ai", "ai-security", "credential-security", "open-source-security"]
description: "OpenClaw is powerful but fundamentally insecure. Why its reputation is deserved, why prompt injection can't be fixed, and how to use it safely."
featured: true
related_episode: "episode-51-agentic-ai-security-full-speed-into-the-unknown"
---

You've probably heard about OpenClaw by now—the open-source AI agent framework that's been making waves. You may have also heard it described as a security nightmare.

Both things are true.

This week, we're diving into why OpenClaw's reputation is well-deserved, what your options are, and—if you absolutely must play with it—how to do it without getting burned.

**What's Inside:**
1. Why OpenClaw is the CGI-bin of the AI era
2. The prompt injection problem (and why there's no solution)
3. Credential storage that would make a Post-It note blush
4. Your two options: wait, or wait differently
5. If you must use it: a security guide for the adventurous

Let's dive in.

---

## 1. OpenClaw: A Brilliant Tool With No Security

Here's the thing about OpenClaw: it was written by a very smart person. But that person isn't a security expert—or at least, they didn't incorporate any security into it. And that matters.

If you were around in the 90s, you might remember when CGI-bin came along. It seemed magical: You weren't constrained to static pages anymore; a website could run programs and display results to users. And to make it really useful, it needed access to databases, file systems, and other data it could get its hands on. And the way to make it most useful, fast, was to simply bypass any security controls and open it up to the Internet.

OpenClaw is like that, except worse.

Today we have access to a lot more data. The things OpenClaw connects to—your files, your APIs, your cloud services—are far more capable than anything we had in the 90s. And unlike a CGI script that does exactly what you programmed, OpenClaw makes decisions. It makes mistakes. Sometimes big ones. Over and over again.

---

## 2. The Prompt Injection Problem: No Solution in Sight

And now for the *really* bad news: prompt injection.

If you're not familiar, prompt injection is when malicious instructions hidden in content—a webpage, a document, an email—trick the AI into doing something it shouldn't. An attacker embeds hidden commands that override your instructions. It's bad enough in a chatbot. In an AI agent with access to your files, APIs, and credentials, it can be catastrophic.

And there is no defense against it. Not really.

In December 2025, OpenAI published a [blog post about hardening their Atlas browser agent](https://openai.com/index/hardening-atlas-against-prompt-injection/) and made a remarkable admission: prompt injection "is unlikely to ever be fully 'solved.'" The UK's National Cyber Security Centre has similarly [warned](https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection) that prompt injection "may never be 'fixed' in the way SQL injection was."

**Why is it unsolvable?** The fundamental issue is architectural. Traditional software has clearly separated inputs and instructions through defined syntax. LLMs process everything as natural language text. There's no reliable way for the model to distinguish between "instructions from the user" and "instructions embedded in content the user asked it to read." Models have no notion of untrusted content—anything they process can be interpreted as an instruction.

AI vendors can block specific prompt injection techniques once discovered, but general safeguards are impossible with today's architectures. There's an endless array of attacks waiting to be found, and they cannot be prevented universally.

**What about defenses?** There are mitigation strategies—layered input sanitization, privilege minimization, behavioral monitoring, confirmation gates before sensitive actions. One [recent framework](https://quantumzeitgeist.com/ai-systems-framework-achieves-multimodal-prompt-injection/) claims 94% detection accuracy for prompt injection attacks. But detection isn't prevention. And 94% means 6% get through—which, for an agent with real power, is 6% too many.

OpenAI's approach is instructive: they're not trying to solve the problem, they're trying to make it manageable. They've deployed automated red teaming systems that continuously probe for vulnerabilities. When attacks are discovered, they patch and harden. It's an arms race, not a solution.

**What does this mean for OpenClaw?** Considering the state of the OpenClaw project right now, it's pretty unlikely they're doing a world-class job defending against prompt injection (and the same can be said for a lot of more mature AI developers). That might (and hopefully will) change, but that remains a reality for now. And with current technology, they can best mitigate the risk to a limited extent.

This is why isolation matters so much. You can't prevent prompt injection. You can only limit what happens when it succeeds.

---

## 3. At Least It Doesn't Use Post-Its

By default, OpenClaw stores API keys, passwords, and account names in unencrypted text files. If anyone gets into your machine, they have everything. If anyone manages to get into OpenClaw itself—say, through a prompt injection attack—they can just ask for those credentials, and OpenClaw will hand them over.

---

## 4. Your Best Two Options: Wait

So you want to try this powerful new tool to see what it can do for you. As of now, if you want to do it safely, there are two ways to go about it.

**Option A: Wait for OpenClaw to improve.**

OpenClaw was written by one person, but there's now a growing community working on it—including the security. If you check their issue tracker, you'll see a ton of bugs being filed and fixed. The architecture has some innate flaws, but it's evolving. Give it time.

**Option B: Wait for the alternatives.**

One of the criticisms of OpenClaw is that it doesn't do anything you can't do with Claude Code or its equivalents. Some security-minded developers have taken that challenge seriously and are building alternatives with security designed in from the start. That's also going to take time, but it's coming.

If you're not in a hurry, waiting is the right call.

---

## 5. If You Must: A Security Guide for the Adventurous

But maybe you need to understand what's coming. Maybe you want to stay current on agentic AI capabilities. Maybe you just can't resist. We get it.

Here's how to play with OpenClaw without putting yourself at serious risk—and as a bonus, this is a great exercise in securing something that wasn't built for security. Which, let's be honest, is something security professionals encounter constantly.

### Use an Isolated, Dedicated Machine

This is one time where we're going to say: don't use a VM, and don't use the cloud.

You want everything local, on one physical machine that you can cut off or turn off, where you're controlling all access. Dedicate that machine to OpenClaw. Don't use it for anything else.

**Why not a VPS?** Here's what's happening: people spin up OpenClaw on a cheap virtual private server because it's easy and "isolated." Then they leave the web console wide open to the internet. Bad guys are actively scanning for these now. OpenClaw's authentication and access control is extremely limited. People are getting popped with nothing more sophisticated than finding an open port.

Unless you're going to run models locally, you don't need powerful hardware. An old PC running Linux will do. An old Mac runs equally well. For some reason, all the cool kids are running out to buy Mac Minis, but that's not necessary, at the very least not to get started.


### Keep It on Your Local Network

Better yet, don't allow access from the network at all, and just access it from the machine. If you do put it on your local network, use a host-based firewall to control access. An isolated machine on a reasonably secure home network dramatically reduces your exposure.

### Give OpenClaw Its Own Accounts

Whenever possible, create dedicated accounts that you only use for OpenClaw. Give it its own local account on the machine that hosts it. Don't give it your personal iCloud credentials or an application password with access to everything.

Even better: create an account and *share* specific resources with it. That way you can cut off access—even remotely from another machine—if things get weird. You want to be able to tell when OpenClaw is accessing something, and you want to be able to shut it down without shutting yourself out.

### Messaging Apps: Same Rule Applies

If you're connecting OpenClaw to messaging platforms like Telegram or Signal, don't use your regular account. Create a separate account that you use only to communicate with OpenClaw.

If that channel gets compromised through OpenClaw, you don't have to worry about your actual conversations, contacts, or message history being exposed. You can burn that account and start fresh without losing anything important. (Of course if the attacker uses it to get access to everything OpenClaw has access to, you've got a whole other set of problems.)

### API Keys: Dedicated, Labeled, and Limited

You'll need to give OpenClaw API keys for Claude, Gemini, or whatever models you're using. Use keys that are:

- **Dedicated** to that OpenClaw instance only
- **Labeled** in the provider console so you know what they're for
- **Limited** with spending caps

That last one is critical. OpenClaw can get out of control. If something fails, it will keep trying. We've experienced this firsthand. Set a low limit when you're starting out—$5 is fine. You don't want to wake up to a $300 bill because it got stuck in a loop.

### Be Smart About Model Costs

Check the pricing for different models. Opus is tremendously more expensive than Haiku, and you don't need genius-level reasoning to check the weather.

Set your default model to something reasonable. You can tell OpenClaw to use a stronger model explicitly when needed, or configure it to ask permission before upgrading.

**A note on console accounts:** There's a way to configure OpenClaw to use your Claude console subscription (like Max plans) instead of API billing. Anthropic apparently doesn't love this and may throttle it, and I imagine the other providers feel the same. Also be aware that OpenClaw will chew through your usage allocation quickly if you're not careful.

Of course you can entirely eliminate those costs by hosting your models on your own hardware, though you're going to need something powerful enough to run them, and that isn't cheap either.

### The Credential Storage Problem

This is the big one. OpenClaw's credential storage is, frankly, terrible. Everything stored in plaintext files by default. This alone is reason enough to be extremely cautious.

**Mitigations:**
- **Least privilege**: If it needs access to specific folders, give it access to those folders only. Not everything.
- **Mac Keychain**: You can configure OpenClaw to store credentials in the Mac keychain instead of plaintext files. It's not bulletproof—someone could potentially ask OpenClaw to pull credentials from the keychain—but it's better than a text file. (Fair warning: this feature is hit-or-miss in our experience.)

### Backup Your Configuration (Carefully)

OpenClaw has been unstable in our experience. The stories about people running it for days doing amazing things? We suspect they're giving it complete, unfettered access—which we don't recommend.

Back up your configuration in case things break. Updates can break things too, and you should be updating frequently given how fast it's evolving.

But remember: your backups contain credentials. Encrypt them manually or use a secure backup system. Don't just copy the config folder to Dropbox.

### Watch Your Conversation History

One common trick is telling OpenClaw to configure itself—connect to a new service, add a new skill. The problem: besides writing credentials to those plaintext files, everything ends up in your conversation history. And OpenClaw saves *everything*.

Be aware of what's accumulating. One approach we've tried: write a directive that tells OpenClaw to periodically scan its own history and memory for sensitive data—credentials, social security numbers, credit card numbers—and delete it. You can have it learn over time what counts as sensitive and ask you about edge cases.

---

## Key Takeaways

- **OpenClaw is powerful but fundamentally insecure.** It's the CGI-bin of the AI era — brilliant capability with zero security built in. The developer prioritized functionality over protection, and the architecture reflects that.
- **Prompt injection is an unsolvable problem.** Even OpenAI admits it can't be fully fixed. It's not a bug — it's a structural limitation of how LLMs process text. Detection frameworks top out around 94%, which means 6% of attacks still get through. For an agent with real access to your systems, that's unacceptable.
- **Credential storage is atrocious.** Plaintext files by default. If someone compromises the machine or the agent itself, they get everything.
- **The best advice is to wait.** Either wait for OpenClaw's growing community to improve security, or wait for security-first alternatives being built by developers who took note of these problems.

---

## The Bottom Line

OpenClaw is genuinely interesting technology, and it's worth understanding where agentic AI is heading. But right now, it's a security liability. Its poor reputation is deserved.

The prompt injection problem alone should give you pause. This isn't a bug that will get patched—it's a fundamental limitation of how LLMs work. OpenAI, with all their resources, admits they can't solve it. OpenClaw certainly can't.

If you can wait, wait. If you can't, treat it like what it is: powerful software with no security, running on a machine that needs to be completely isolated from anything you care about.

And finally, all of this is changing, on a daily basis (the project name itself changed twice in the space of a week). If you're going to jump in, do your best to stay up to date.
