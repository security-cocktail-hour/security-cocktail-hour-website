---
title: "AI attacks need AI defense: Ransomware's new danger and how a top cyber expert is fighting back"
date: 2025-09-23
draft: false
guest: "Karen Lagziel"
category: "AI"
duration: "57:33:00"
image: "/images/episodes/episode-061.png"
description: >-
  Everyone's using AI, including ransomware gangs. Podcast guest Karin Lagziel, Director Cybersecurity at consulting firm Sygnia, gives us the news and her cyber defense strategies for fighting back: With more AI, as well as a focus on fundamentals.
platforms:
  youtube: "https://youtu.be/iYf6ZS7HTzg"
  spotify: "https://tinyurl.com/4rbpye89"
  apple: "https://podcasts.apple.com/us/podcast/security-cocktail-hour/id1679376200?i=1000728053274"
  amazon: "https://music.amazon.com/podcasts/d11e431a-f7b1-4bb0-8671-024afce9ade6/security-cocktail-hour"
guest_bio: "Karen Lagziel, Director of Cybersecurity Services/Sygnia"
---

Everyone's using AI, including ransomware gangs. Podcast guest Karin Lagziel, Director Cybersecurity at consulting firm Sygnia, gives us the news and her cyber defense strategies for fighting back: With more AI, as well as a focus on fundamentals.

## Episode Highlights

### Listen Now

Tune in to hear our discussion on ai attacks need ai defense: ransomware's new danger and how a top cyber expert is fighting back.

## Key Takeaways

* The first AI-powered ransomware "Prompt Lock" discovered in the wild
* How Chinese hackers created "Villager" - the AI version of Cobalt Strike
* Why traditional cybersecurity is failing against AI attacks
* How attackers weaponize your own AI against you
* The dark web's "AI as a Service" marketplace
* Real-time deep fakes so realistic they fool security experts
* AI governance frameworks
* Why every organization needs agentic AI for defense
* The future of cybersecurity careers (spoiler: humans aren't going away)

## Resources Mentioned

Villager: https://thehackernews.com/2025/09/ai-powered-villager-pen-testing-tool.html

Cobalt Strike: https://techinsightzone.com/cobalt-strike-in-cyberattacks/

FAA Part 107 Drone Pilot License: https://pilotinstitute.com/part107-license-guide/

Executive Order on AI: https://www.whitehouse.gov/presidential-actions/2025/01/removing-barriers-to-american-leadership-in-artificial-intelligence/

NATO Article 5: https://www.nato.int/cps/en/natohq/topics_110496.htm

PromptLock: https://www.eset.com/us/about/newsroom/research/eset-discovers-promptlock-the-first-ai-powered-ransomware/

Albania's AI corruption minister: https://apnews.com/article/albania-new-cabinet-parliament-ai-minister-diella-corruption-5e53c5d5973ff0e4c8f009ab3f78f369

AI surgery: https://healthjournalism.org/blog/2025/09/ai-is-enabling-robots-to-assist-in-surgery-what-to-know/

## Full Transcript

**Karin [00:00]:**
Every organization eventually must defend their organization with AI,

**Joe [00:10]:**
Welcome to the Security Cocktail Hour. I'm Joe Patti.

**Adam [00:13]:**
I'm Adam Roth, I think.

**Joe [00:16]:**
You think, no, I know you're Adam Roth and it's a good thing because we got a good show today, Adam. We have one of my favorite type of people on. We have not just a consultant, but a consulting manager. And I love consultants because they just see everything. They get a whole view of the whole world, not just like what their company's doing, like you. You only know one thing.

**Adam [00:42]:**
Me? I know, do know

that consultants are really good at bringing in revenue if they know what they're doing.

**Joe [00:48]:**
That's true. It's actually a little joke about Adam that he has more side jobs and professions than anyone else, but that's a whole other story. But in the meantime, we have Karen Lagziel. Karen, welcome to the show.

**Karin [00:56]:**
Thank you. Thank you for having me. Hi, everyone, Joe, Adam. My name is Karin Lagziel. I'm a director of ⁓ cyber services at Sygnia, and I've been at Cyber Security Consultancy, as Jo mentioned, ⁓ for 15 years now. So, very excited to be here and talk about my favorite topic.

**Adam [01:23]:**
15 years, you don't look like 5 years over 20.

**Karin [01:26]:**
I started when I was three.

**Adam [01:28]:**
Good job.

**Joe [01:30]:**
Yeah, it's good to see young people in the industry. That's cool. you know, we know it's interesting. We know Sygnia for quite a while. We've just haven't work with them for a bit. But we haven't actually worked with you, though. I think you started after we, since we've not been working with them so much. And you're a little unique because I think, well, you're not the first, but you are Israeli, of course, but you're not from 8200.

**Karin [01:46]:**
Yes. ⁓

**Joe [01:58]:**
and you're in cyber and Sygnia, right?

**Karin [01:58]:**
I moved out from Israel to New York about when I was...

So I kind of skipped that and started my career in cyber consultancy and didn't go kind of the different route that you know today as of a lot of Sygnia's staffs are from 8200 and a lot of great Israeli cybersecurity startups as well. Yeah.

**Adam [02:30]:**
Joe, do remember how we found Karen?

**Joe [02:32]:**
Why don't you tell me how we found Karen?

**Adam [02:34]:**
a year ago almost this month, I mean maybe next month, but ⁓ we went to Cybertech, not we specifically go to Cybertech, but we saw her speak at ⁓ New York City Cyber Tech.

**Joe [02:46]:**
That's right, pays to go to conferences, you can be fabulous people.

**Karin [02:47]:**
Yeah, yeah, that's correct.

Yeah, I get a bit about, we talk about cyber security, AI security, and all the fun AI matters, of course. It was a fun conference. It was great to see you guys there.

**Adam [03:03]:**
I wasn't saying myself, I'm trying to get more on the conference ⁓ trail. I just came back from Government TechCon in Washington DC and I gotta tell you, when you go to ⁓ a tech conference, you really do learn a lot, not only from what people are saying, but from the people that are there and what they're speaking and what they're feeling and what they want and what they need. So it was great to meet you there and it's great to go to any conference these days.

**Karin [03:31]:**
Yeah, I agree. think a lot of conferences that I lately go to I'm sure you as well, know AI is a big obviously ⁓ topic in those conferences, but I think it's as you said, right? It's it's great to see a lot of different industry leaders whether it's if insecurity or legal or you know financial or healthcare doesn't matter or different kind of of sectors as well, but it's it's great to learn from them kind of from their challenges dealing with AI I feel like AI is very fairly new to all of us, we all struggle in different aspects, whether it's a governance or security or adoption or from CISO to staff. ⁓ So it led me as well, Adam, of similar like you, to really learn from other ⁓ leaders what are their biggest challenges and kind of just share and kind of community to share knowledge and to learn from each other. So I really like that as well.

**Joe [04:26]:**
Yeah, well, I've been looking forward to us talking here because ⁓ you mentioned AI in the first five minutes, which is great. And I have an AI question that's kind of current. So we're going to get some free consulting too. ⁓ I saw there is that new thing. What are they calling that? Villager. They say it's the new AI version of Cobalt Strike, where some Chinese outfit put together, ⁓ I guess like an agent-based AI thing that just goes and...

**Karin [04:38]:**
sure.

**Joe [04:56]:**
acts like crazy, does ransomware and that at least a week or so ago. And, know, it just struck me because, you know, if we've talked about AI on the show before and in other places, and when you keep hearing like, yeah, it's making people work faster. It's, you know, people are writing code with it and everything. But we hadn't really seen anyone really leveraging the technology in a fundamental new way from a security perspective. This looks like it might be.

**Adam [04:59]:**
Yeah, I just saw that too.

**Joe [05:26]:**
I was curious if you guys have, if you can talk about it, if you've bumped up against this or anything like it lately.

**Karin [05:34]:**
What I see ⁓ from security perspective or clients of ours that adopting some kind of tools, I do see that all of the big tags and all of the solutions are expanding to AI models. So I think from business perspective, that's your competitive edge. And also you have to kind of advance with the AI in the wrong hands, which we call it, the good and evil battle. ⁓

see a lot of use cases being applied in cyber security. course, outside of cyber, that's ⁓ in every aspect of organization from finance to HR to legal to auditing assessments, right? But in terms of security, and again, I'm not going to call out specific names or vendors, but I think there is a good ⁓ evolution that I see here that using more and more agentic AI.

We started with Gen AI, which was great. We were able to more use it for call centers or, you know, text summarization, things like that. But in cyber, we see a lot of SOC augmentation. So basically using a lot of those repetitive tasks of analysts that help them to summarize in a large or to do threat hunts, do like kind of AI red teaming and autonomous identify vulnerabilities. So I see a lot

of those areas that are being applied. But I also see that we need to continue to kind of develop in those and monitor the effectiveness and model drifts, right? Because not always you can trust the results. You need to insert a lot of quality data and monitor that continuously. And it takes a lot of power and commute. It's much more complex than that. I do think we are getting there. And it's getting actually faster than ever.

I think the new thing is really agentic AI, which is the more autonomous way of defenders and how we apply that.

**Adam [07:43]:**
I'm gonna

throw a couple curveballs in here. When I went to this government tech conference, I met some government contracting companies or companies that wanna sell the government contracting companies. And there was like two or three things that we spoke about. One was one vendor has an LLM that can ingest video in real time and alter the video via AI.

Remove objects. They don't want people to see on the screen and I'm going to believe that In real time. So basically there's an interception of that stream that stream turns around and we writes the video and remove certain things for me and I think it has some ⁓

**Joe [08:15]:**
In real time?

**Adam [08:29]:**
government use the other AI Person I spoke to his job is to utilize AI to help government contracting companies get government contracts So it writes their bids and puts things together in such a way that they can get government contracts the third thing I'm going to talk about is Yeah, I'm gonna brag. I just passed my FAA 107 UAV or drone certification

But there's something called the FAA 107 waiver for beyond visual line of sight and there's also a new one coming out called the FAA 108. Why is this important in AI? Beyond visual line of sight meaning you don't watch the drone where it's going, you're flying it autonomously. AI now is doing everything it can to have collision, ⁓ deference so your drone doesn't crash into other drones.

**Karin [09:00]:**
Congrats.

**Adam [09:28]:**
Recognize objects, you know how to fly around them and those how to alert on them. So it's really interesting how a how These these drones now, it's kind of like your car, know You're driving your car and it sees a car but it breaks it does the same thing for your drone But the more advanced the AI gets with the drone the more it's able to recognize objects notify you of objects Call out verbal commands and things to let you know like, know, like how you hear a plane

**Karin [09:40]:**
Mm-hmm. Yep.

**Adam [09:58]:**
Like pull up pull up, you know something like that that drones gonna tell you all that stuff. It's

**Karin [10:05]:**
Yeah, think that exactly like that's the LLM, right? Like that's the kind of advancement that we see with Gen AI, which before it was more a rule base or, you know, we had AI, we had some machine learning, but I think exactly the beauty of it is the real time, a large amount of data analysis, whether it's text and videos and images, and then based on specific model, right? You teach the model what you want to flag or what you don't want to identify. This is good. This is not good.

stop when you see some break, right? ⁓ I think that's what really kind of the game changer that we see over the years, right? Before it was, again, we had machine learning and everything like that, but the amount of interpretation that ⁓ LLM can do, and then if you mix it with, integrate it with AI agents or agentic AI that can actually take this data that you talked about, Adam, and then actually really ⁓ perform action, right? Perform action on that.

**Adam [11:02]:**
on it.

**Karin [11:05]:**
and making decisions, but also this is the scary part. You mentioned drones or ⁓ car that, really from safety perspective or from military intelligence, things like that, AI models bring a lot of concerns and risk, especially in those models if we're talking about ⁓ prompt injection or poisoning models. So those are just a lot of different type of obviously

threats that we have now to from trade threats framework that we work on when we're trying to understand What is my model? What are the threats and risk with my model? So for example poison it data poisoning it can be to miss miss classify a stop sign with go right so for example I think they actually had in the prototype of Tesla or something something like that happen if I'm not mistaken Yeah

**Joe [11:56]:**
you

**Adam [12:02]:**
vote about that. Yeah.

**Joe [12:03]:**
it's happened a lot. Yeah.

**Karin [12:04]:**
Yeah, and

**Joe [12:05]:**
Yeah.

**Karin [12:05]:**
that's if you think about it, we move in outside for a second from cyber aspect of that and the use cases in cyber war. I mean, it's part of that, but it's more fundamental risk of safety. And I think that's the White House executive order, the AI bill, talk a lot about safety from those perspective as well. ⁓

**Adam [12:27]:**
Yeah.

**Joe [12:27]:**
Yeah, that's

what worries me about the agentic stuff because they say, it's independent. It can make decisions and everything. ⁓ That's great. As long as it's making good decisions, you know.

**Karin [12:35]:**
you.

**Adam [12:38]:**
So

yeah, I write about cyber ethical warfare and one of the concerns that I have is that if you're a nation state and you're going up another against another nation and ⁓ That nation has you AI utilized and then you poison that AI by LLM injection and you make now the friendly tanks the opposition tanks You're attacking your own you have no control. You've already compromised that that AI that LLM that network

**Karin [13:03]:**
Yeah.

**Adam [13:08]:**
to seek out its own tanks, own planes, its own soldiers. This is a different war that we're, this is a, the next war like that, it's gonna be a very different war.

So one of the things I write about is NATO NATO article 5 which basically is an attack on one It's an attack on all and the collection of nation the collection of states that belong to NATO They basically talk about what is an attack and what's not an attack, but what's not clearly defined now with cyber warfare

Cyber warfare incorporates AI we what they do talk about is biological radiological chemical and kinetic war but what if a nation does inject and Does cause another country to seek out its own against against Geneva Convention or whatever? We want to talk about whatever frameworks are supposed to be ethical and you start destroying your own country because you were compromised by another country It's crazy stuff happening

**Karin [14:04]:**
Yeah, we call it, sometimes I hear the terms and we use it a lot as well, a double agent, right? It's actually a legit AI model that you implemented and trust within your organization. ⁓ But then it becomes, the attacker weaponized this model, so it's become ⁓ AI attack. ⁓

basically using your own model. So it's basically the prompt injection is attacker manipulating instructions, if you will, right? The instruction given to the AI model, it gives the instruction that to ignore the safeguards, the controls, then it, the hidden malicious actions. So eventually it's kind of similar to SQL injection, if you're familiar with that method, but in AI world is a bit more complicated and complex. Essentially it's

It's effectively a hijack ⁓ of the model.

**Joe [14:59]:**
Well, it's

interesting because it's more complex in one way, but it's less complex in another because we're used to things being hacked. You can hack it, you break in, you compromise it, you can take control and do all kinds of stuff. Okay, and that's hard. That's not easy unless something's written really badly. Now with a lot of these AIs and these models, the underlying of, I don't know, guts of how it's working is very complicated.

But it all seems like with the LLMs with some of these things like prompt injection, I can't help the feeling that it's like, okay, now with machines, we can try to actually talk a machine into doing something. Like you could with a person. And so far, they're particularly stupid people who fall for things that a person would say, this is ridiculous. That's what worries me a lot.

**Karin [15:50]:**
Yep.

**Adam [15:52]:**
But then you have those other people

that are doing the opposite, right? They are jailbreaking whatever AI, LLM. They're going on to a website for a car dealership and convincing that AI agent to give them a free car and they've gotten it. They're convincing these agents that give you pricing to give them a lower price. It's kind of like there's nothing to see here like Star Wars.

**Karin [16:20]:**
Yeah, I think you mentioned Joe something. ⁓

**Joe [16:21]:**
The Jedi mind trick.

**Karin [16:27]:**
very true to the scary part, right, with, for example, prompt injection or jailbreaking, is that as it used to be, right, you explode the bug in the code. So you have a lot of controls around the code and you kind of were able to isolate and understand where it's coming from. Whether when we talk about ⁓ AI LLMs, it's exploit how the model itself works. So imagine it's actually out of the computer, how the system works. So it makes it harder to detect

to patch even. And if attackers succeed, it can just literally trick the AI, giving you, as Adam just mentioned, trick you to giving you sensitive information, bypassing control, telling you, this control whitelist me or don't block me or things like that. So again, it's become very, very complicated because there is kind of like three level of that, right? If you will, every time I try to speak about ⁓ AI cybersecurity,

I see it in really three levels. One is when attackers can now use AI. There is a lot of software in the dark web. There is impersonation, deepfakes. They don't need to be smart anymore. mean, you know, some of them were not before, but saying that the bar is very low. They don't need to know a lot of coding. They don't need to have a lot of money even. They just need to ⁓ have the motivation. And then the second part will be the AI

⁓ AI defense. So how can we use the AI technology and agentic AI to advance our defense mechanism, right? Because the security controls that we have are no longer enough or will not be enough in the near future. And then the third is, now that we implementing AI and all those models in our organization, not just cyber, right? Think of a dozen of use cases for each business unit. Everyone wants efficiencies and right to use that.

But now there is expanded attack surface, expanded vulnerabilities, configurations, API, external servers. So it's really those kind of three, I don't know, it helps me to kind of see it in three layers, hopefully that help you as well. this is how we start breaking it down and put together those frameworks with our clients.

**Adam [18:52]:**
So,

**Joe [18:53]:**
The third one really scares me because I think the attack surface has just exploded, especially now with the agents and with MCPs and there you go. I've seen it using Claude Desktop and it says, connect to this, connect to your file system, connect to here, connect to there. And you're like, well, wait a minute, this is some serious stuff. a lot of the code that's out there, I mean, there's some nice people doing a lot of code and everything and it's in GitHub, but...

even before we get to malicious, is it safe? it been tested in a rigorous way? giving it access to your file system or your personal stuff or like the Dropbox account, inboxes, stuff like that. And they go, to really make it valuable, you got to give it access to all these things. And I'm like, ⁓ I don't know if I really want to do that. I don't like my provider being able to see my email, much less someone else.

**Karin [19:35]:**
inbox here. ⁓

**Adam [19:46]:**
Or yeah But yeah, but think

**Karin [19:50]:**
Exactly.

**Adam [19:51]:**
about that right the LLM they kind of convinced it that they were gonna shut it down and Then they kind of injected false information into it and the LLM is like well if you shut me down I'm gonna email your wife that you're cheating on her Do you remember that one that was recent? So so I don't know man. There's some rogue LLMs

**Joe [20:07]:**
Yeah.

**Karin [20:08]:**
Yeah.

Yes, becoming double extortion. But yeah, I think to Joe's point, it's even broader than that. That's what we deal with right now, the big concern of shadow AI, right?

So back before, who have the access to really play with machine learning and automation and all that. was kind of like science, data science people and engineering and you don't have access and it's very secure. Now every web app that you have everywhere from any user can just download something, can connect as you said, right? connect me to your inbox. A lot of users do that and CISOs and Infosec

leaders in organizations don't have, sometimes they don't have visibility to that. So where it does start is with education. We need to have training to these users in our organization. You need to tell them what's the risks here. For example, I have a user that I know that used GPT back in the days before it was even kind of like, you know, allowed to use in organization or blocked and started to put PDFs in Excel, started to upload.

a lot of sensitive information, just as to summarize information, right? But basically that resulted in leaked sensitive information. So sometimes people don't know what they don't know. I think it's any other cybersecurity awareness and training. This must be a top priority, which it is. I see it now across a lot of organizations. So that will be first. And then of course, have security controls, block as much as you can or monitor it.

at least, but yeah, that's a huge concern. I absolutely agree with you. We used to have shadow IT, now we have shadow AI, which is a much more bigger monster, if you will.

**Joe [22:03]:**
Yeah,

and a few months ago we had another guest, Kevin O'Connor, on and he was saying like, you know, it's the next generation of shadow IT and he goes, it's shadow development because now everybody's a coder. And, you know, as if that weren't dangerous enough, apparently I've been reading lately that a lot of this vibe-coded stuff is actually really low quality, that it doesn't work well besides. So,

**Karin [22:16]:**
Yep.

Mm-hmm.

**Adam [22:32]:**
So Karen, I'm paranoid. I don't think Joe knows that yet. And my thing is, yeah, we're going to use our own enterprise, our own sandbox AI. Nothing's sandboxed. Everything is interconnected. Somebody can move laterally from your enterprise, LLM. I don't even want to have access to my own inbox. ⁓

**Karin [22:42]:**
Mm-hmm.

Amen.

Understood.

**Adam [22:59]:**
How

do people feel about using their own AI ⁓ instance in their organization? Are they worried about it? they concerned about it?

**Karin [23:11]:**
They do, ⁓ of course, but...

I don't think fear should stop you to evolve with technology and eventually you will lose competitive edge and even operational effectiveness, right? So yes, I hear these concerns. Yes, there is a way to do it step by step. We need to have baseline. We need to have governance and controls and risk assessment and AI inventory. This needs to go through the right channels. have committees, AI committee.

which means you bring a use case even if it's just enabling.

some kind of existing software, right? If you already have a software and they enabled AI, you need to understand what it is. Before that, you used to do third-party security assessments. That's calling it right now as well. And understand what does that mean? If I give access, I just worked with a client that was about to give entire access, full control to his inbox. And then we started to kind of narrow it down and go to configuration and say, okay, read only. You cannot write an email for me.

you cannot send because then we already have ⁓ some research about the AI assistant inbox that basically was able to leak information or even just draft some fake invoices or request for payments, right? The list goes on. I agree with you, but I do think that there is a way to work slowly with the right governance in place, which is the key, ⁓ but not to go backwards and not to fear.

**Adam [24:27]:**
You

**Joe [24:34]:**
Yeah.

**Karin [24:48]:**
I do think if your security strategy does not include agentic AI today, you're preparing for yesterday's threat, right? Not today reality and not to the future. So I think it has to take place, but with process, the right process, the governance, as I mentioned, policies and the right procedures.

**Adam [24:57]:**
Yeah.

So full transparency,

I'm a little bit behind the eight ball, right? I really haven't been involved in Enough cyber stuff in my life, especially with AI. We had a woman on Yeah, that's what I'm doing so so we had a woman on last episode her name is yeah She just started doing auditing of blockchain So my question to you Karen is is that something that's happening now where you literally have a whole entire framework to audit?

**Joe [25:19]:**
Because you're flying drones around all day instead of doing cyber like you should. Please.

**Karin [25:22]:**
That's fun.

Mm-hmm.

**Adam [25:40]:**
order people's AI? Is it really that structured these days?

**Karin [25:43]:**
No, it's not structured at all. We do have frameworks. are tons out there, right? OSP, Threat, and ⁓ LLMs, and NIST, and there is tons of information out there, which is good and bad as well.

almost drowning in that, but also there is a lot of help from community, from public and private. ⁓ No, it's not straightforward. Every AI needs to understand, it in-house builds, is it fine-tuned, is it just calling APIs, is it some SaaS and Microsoft co-pilot, which can be more structured, yes, but it's very depend on your environment. it's, I would say it's very customized as well. We do have the areas, the threats.

modeling the frameworks, a lot of those kind of areas, identity and access management. There's a lot of AI agents service account that are a huge gray area and what do we do with those? And there's just tons of threats and risk to look at. But yes, if you work slowly but surely, you are able to scale your AI in the future versus now you're trying to just control it, an AI here or there.

enable some kind of model here and there, but then you just drown in with it because it's just going to go more and more, right? You're going to adapt in ⁓ very rapidly, especially all I hear today from security side from CISOs is the business pressure on them to do that. So that to us, that means that this will not stop. It will continue to grow. And you have to take control over that by governance and inventory and risk assessment and things of that nature.

you

**Joe [27:29]:**
Okay,

now that you've got into the thing, that's kind of the real heart of it that there's always been the tension between we need to do this now, we need to do this new technology, and AI is moving faster and is more dangerous from a security standpoint than ever before. And that means it's time to take a drink because I need a drink if we're going to talk about AI governance and stuff. So I got wine. What do you got there, Karen? You got something interesting, right?

**Adam [27:49]:**
Alright, we're...

**Karin [27:50]:**
Yes.

Yes, I have sake, my favorite drink here. It's actually straight from Japan. My sister just came back from her honeymoon, so I got her real good sake. Cheers, guys. What are you having? Wine, I see. Yes. ⁓ that's nice. Jack Daniel. ⁓ never saw that before. Watermelon. Well, Joe, would guess it's coming from...

**Joe [27:58]:**
You have sake.
Oh, the good stuff. Cheers. I was too scary to have sake. Yeah, I got a uh, think it's a little Chianti there. And what do you got there? Jack Daniel's Watermelon?

**Adam [28:05]:**
Nice.

**Joe [28:16]:**
You guys are drinking some stuff that just takes a party to the next level. I feel weak.

**Adam [28:19]:**
Jordan? No, Jordan is like

drinking seltzer.

**Karin [28:24]:**
Yeah, I would assume this is coming straight from Milan, which you just came back from, this beautiful wine, or no? No.

**Joe [28:26]:**
Thank

⁓ No, not really.

is, well this is actually, actually it's not from Milan. It's not from Lombardy. It's actually Tuscan. You know, it's interesting. Yeah, one of the things that's wonderful about Italy is like, and a little diversion here. I'm just back from Milan. I'm always back from Italy it seems, but you go to the supermarket and the supermarket is wonderful. The supermarkets there are like a gourmet shop besides all the excellent shops they have.

**Karin [28:39]:**
hmm my favorite

Thank you.

**Joe [29:00]:**
But the wine is like four euros for like a halfway decent bottle of wine. I'm like, God, the same stuff you'd pay like 11 bucks for here. I'm like, ⁓ how are these people not all drunks in that country? I don't know. I don't know.

**Karin [29:04]:**
Okay.

Yes.

50 yeah,

**Adam [29:13]:**
So, Karen, let me ask you a question.

**Karin [29:17]:**
That's why they're all happy. Yeah, exactly. They look

**Adam [29:17]:**
Who says they weren't?

**Karin [29:20]:**
so happy and healthy. Amazing cheese. Yes. Yes.

**Adam [29:22]:**
So let me ask you a question. don't want Joe to hear this. What would you do

if somebody went to Milan, something was inexpensive and didn't bring back a gift? How would you feel for your business partner, podcast partner?

**Karin [29:34]:**
I would ⁓ strongly consider

the future of our relationship.

**Adam [29:39]:**
Thanks for giving me insight. Thank you.

**Karin [29:41]:**
Yes, especially from Italy. ⁓ But I'm not just inside here, guys.

**Joe [29:45]:**
Okay, I'm going... I'm going back. I'm... you... No, you know what?

**Adam [29:47]:**
you

**Joe [29:52]:**
Okay, I'm gonna be back there in a couple months and I am bringing you back the cheesiest, corniest, most touristy souvenir I can find. Okay? That's okay with you.

**Karin [29:55]:**
Okay.

Yeah

**Adam [30:02]:**
That's okay with me Joe Do know what I used to remember? You know,

funny right back in the day when Sygnia was our was our vendor They used to send us like wine all the time. That was nice though Remember those days like we get like a box of stuff. It was nice Yeah

**Karin [30:14]:**
I We still get those.

**Joe [30:19]:**
Well, I assume it's still good. They used to send us good stuff. I one time I opened up that package and I know a little bit about wine. I'm like, whoa, this is good. And my thing would always be like, oh, we get a bottle of something. We'll have it on a Friday afternoon. We'll share with everyone. And I'm like, I'm going to keep this one for myself. This is pretty good. That's right, back when they were a teammate.

**Karin [30:20]:**
Not you. ⁓

**Adam [30:21]:**
I know that!

**Karin [30:25]:**
Yeah.

Yeah. ⁓

**Adam [30:40]:**
Joe, go so far back with them, they were Team8.

**Karin [30:44]:**
Mmm, wow. Wow.

Amazing.

**Joe [30:48]:**
And you know, okay, we talked a little bit about AI. One of the things we used to deal with them a lot, it was ransomware. And you know what? AI is getting all the attention. But the last time we checked in with someone talking about ransomware, they said, no, it's still there. The incidents, are lot of, it's all ransomware and stuff. How are things looking these days, Karin? Give us a check in on that.

**Karin [30:57]:**
Hmm.

Yes, ⁓ absolutely. ⁓

**Adam [31:12]:**
I hear varying things.

**Karin [31:17]:**
I

mean, yes, absolutely. It's growing by the minute. Unfortunately, as I mentioned, ⁓ yeah, of course, it's been successful for them. It runs as a business, as an organization for everything. They have ransomware call centers and they have hierarchies and they have really serious threat actor groups. unfortunately, we still deal with a lot because it just proves to them as successful.

**Joe [31:21]:**
growing still.

**Adam [31:33]:**
Yeah

**Karin [31:47]:**
⁓ We see a lot of more advanced techniques as well. So we see the capabilities are evolving and talking about AI, this is exactly the problem because right now it used to be more, you know, very complex groups and nation states, right? The very kind of for, if you have a kind of a graph, this will be here, like kind of opportunistic hackers, right? And that kind of nation states. Now it's blurred with the AI. Everyone have in the dark web, you have

fishing as a service, have AI agents, malware spreading, autonomous spending spreading. There's just a lot that you can do.

**Joe [32:28]:**
⁓ on the

dark web besides the regular stuff they're sharing, now they're sharing agentic stuff, AI stuff too? really?

**Karin [32:34]:**
Oh yeah, absolutely. There are tons

of tools in the dark web that runs as a service. like if you, for example, if you have a vendor, Microsoft, right, as a service, this is just a similar kind of AI as a service or phishing as a service, ransomware as a service. You have all of those in the dark web, which is, makes it just so easy for attacker to do that even more. You don't need to code anymore. There are ransomware that AI, AI agents and open source models that can

help

you do that. And actually, ⁓ I think it was in the... ⁓

the ESET ⁓ research recently. I'm sorry, I'm just not remembering that. it actually have a very interesting showing that the developing of ransomware recently discovered by AI. So AI powered first ransomware discovered by them. ⁓ you, yeah, just you can look through that. It's very interesting, read it, ESET, it's called prompt lock. So I remember when I read it, it was more,

**Joe [33:31]:**
⁓ really?

**Karin [33:41]:**
It's really showing you how it's using generative AI directly during the attack execution. not before, ⁓ absolutely. Just think of the power that AI agents have today and what it will be. mean, is every, it models evolving every three weeks, right? We're not even, we can't keep up anymore. And we're not even talking about ⁓ Reg and AGI, which is completely different. ⁓

**Joe [33:51]:**
So it's happening now. They're really doing it. Wow.

**Karin [34:11]:**
aspect to this whole technology, right, which the big tech already working with. But yeah, we actually we had it at Sygnia. We we developed that in the lab, but it was even like two years ago. It was even still before this all, you know, the big LLMs and the agentic AI and before the kind of more advanced, I would say, technology. And we're able to showcase. We call it Viper AI. ⁓

evil ⁓ model Viper. So basically what we did in all right you have the kill chain right so in all steps of the attack you're able to use AI model so reconnaissance go through all LinkedIn web everything to get information or even as a target summarize to me which targets I should focus on and why right less more more exposure less ⁓ less regulation maybe things like that reconnaissance was

was

able to identify a person from IT in LinkedIn and then ⁓ able to identify some WordPress external ⁓ surface and then writing the ransomware code and deploying very interesting ⁓ use case to show. And I'm just telling you it was two years ago. We showed it actually. We demonstrated a teammate. You mentioned teammate, right? Every year they have events.

We really did that kind of research and showcased that. And it just showed you that you don't need now a lot of human intervention. So if you're an attacker, now today you need to sleep, to eat, you need maybe some funding, you need some skills, you don't need those anymore. You can also do it in parallel, multiple targets, you don't need to sleep, you know.

**Joe [35:46]:**
⁓

Wow.

You know,

now I know why you weren't too impressed by the villager stuff when I brought it up, because you had this stuff two years ago. That's pretty impressive.

**Karin [36:14]:**
yeah, weirdo.

**Adam [36:15]:**
I find

it really cool now that you know, and not that it's now it's been for years But you know people do ransomware as a service like it's eBay or Amazon So people stand up their ransomware the cobalt whatever it is And then they work with other people who are affiliates and those affiliates use their agents But they populate those agents where they're in code their codes their Affiliation code so that when ransomware happens

They get a percentage of that money from the infrastructure that's already been stood up. So it's like, it's amazing. Like, ⁓ I'm affiliated with this organization's ransomware. I send out their agents. If it gets done, they send me a certain amount of money, but they use their infrastructure and the money goes to them and I get a percentage of it. It's really cool. I don't approve of it, but I'm just saying it's an interesting business model.

**Karin [37:04]:**
Yeah, cool for them, yes. Yeah,

yeah, and it's only growing. And I think also, yes, we talked about...

AI agents and using AI and LLMs to actually ⁓ execute an attack in real time again. But also don't forget where most of a lot of our ransomware coming from still phishing, right? Impersonation. Of course, there are still I'm talking about some misconfigurations and third parties, of course. I'm saying still a lot of those come from phishing. AI, Gen. AI now have very realistic and deep faking and voice.

and images in real time, even conversations that they can mimic, which really increase those kind of fishing at the success rate, right? Because even if before you had those awareness and now users know how to look at mistakes, no mistakes now. Jenny and I have grammar checks and images. can literally impersonate a person. ⁓ I saw an article kind of using some tool.

**Joe [37:50]:**
Yeah

Yeah.

**Karin [38:14]:**
creating your fake ID and just very impersonation, creating your website if you're a company, creating fake website, LinkedIn, just I'm talking about like taking it for you know even espionage or nation state, there is just a lot, just enough with deepfake and phishing, let alone all the other things that we talked about as agentic AI being used by attackers. So yeah.

**Joe [38:42]:**
Yeah,

you know, originally when I guess going back, God, it's almost three years when the first gen, I think, exploded. You know, we started worrying about, wow, okay, now we're not going to be able to tell that the person who wrote this, that their English isn't so good or whatever. But they've gone a little bit, but they've gone so far beyond that from what I understand. And not only is it, you know, native speaker level for whatever the language is.

**Karin [38:58]:**
exactly I still get those a little bit and I'm like haha I'm laughing I'm like okay yeah yes

**Joe [39:11]:**
But also, like you're saying, they're doing like they can use specific industry terms. If they get a hold of someone's email in a company, they'll use like, you know, the acronyms and kind of their own company speak what they do. Like, wow, that's tough. Yeah, that is tough.

**Karin [39:22]:**
Yeah, exactly. In seconds.

Yeah, it used to be

you need three months to rent somewhere and now it will be two days, right? So also we're talking about the changes of the time, the duration, the implications, the sophistication, which really means, again, we're going back to the same kind of point that we talked about. Every organization eventually must defend their organization with AI, because if they're fighting with AI, you need to fight with AI with a real time adaptation.

and more predictive, able to analyze vast amount of data from different sources in real time. No human can do that and no system can do that even as of today. So yeah, this is the future we're looking at and I would say we're working a lot with the kind of first steps we talked about, right? It's the strategy. Let's talk about a little strategy, take a little low risk scenarios first, right? Maybe internal that are not

something externally used by customers and no sensitive information. So you can still, you start with that. You start with some governance around AI agents and governance around, in general, AI. Yeah, and you go.

**Joe [40:42]:**
Okay,

I know that's the right answer, good governance and everything, but governance is boring. The bad guys have all this cool stuff. We've talked a lot about the threat side and the offensive side. ⁓ What do we have on the defensive side though? Yeah, yeah. How do we fight back? That's it.

**Adam [40:47]:**
You

That's just gonna ask that yeah But I want to qualify that Joe. I know there's better tools

to defend against it. My question first is What tools do you have if any? to reverse the ransomware to inject keys to compromise to to To I guess to find a way to not have to worry about getting their keys from them Is there a better ways to unencrypt ransomware without their?

use their help. No, right?

**Karin [41:29]:**
Yeah.

I wouldn't say no. I'm not familiar with anything at this point. don't think we have. I've seen anything like that. I think we still have the same concerns. Let's not forget, yes, maybe we increased and adapt ⁓ new and advanced technology, but the goal is the same for attackers and haven't changed. The goal is to get money ⁓ most of the time, right? If it's not nation state or espionage, but ⁓ that's what they do. And then the company will have to make decisions, pay or not pay.

see if they have backups, see if they understand, ⁓ maybe if they have better logins and understand what kind of data was exfiltrated, they will be able to make better decisions. But ⁓ we cannot fight yet ransomware. Like I wouldn't say, we have a tool for defensive. There's no one magic tool. You have to just start building AI agents and models in every aspect. Like, like right now you have teams of humans in information security, right? You have analysts, have engineers, you have

⁓ any type of different roles, those will need to be augmented with AI agents. Eventually analysts will be AI manager, right? The future is that we will manage the AI agents versus we'll make them kind of do the work and then review their outputs and kind of work with that.

**Joe [42:42]:**
Yeah, I've...

**Adam [42:49]:**
Yeah

**Joe [42:51]:**
Yeah, I've heard that's

the trend that basically the tier one analysts, as if they weren't threatened enough by plain old sore, they're going away and it's becoming more like, yeah, agent manager.

**Karin [42:54]:**
Yeah, for now the tier one, yeah. Yeah.

**Adam [42:58]:**
What country in

What country

**Karin [43:02]:**
Yeah.

**Adam [43:02]:**
now just put in place the AI manager that manages corruption? They got rid of a human It was Albania or Croatia Croatia

**Karin [43:08]:**
⁓ Yes, maybe. Anti-North

**Joe [43:12]:**
What's this?

**Karin [43:15]:**
Croatia? I know what you mean. just saw it.

**Adam [43:17]:**
But whatever it is, have a co- They're

like, we don't need a body anymore. We're gonna have this AI agent managed corruption. It was like, what?

**Karin [43:21]:**
AI governments,

Well, it started, again, it's more I kind of read actually by it was interesting to me, but it's what we're going towards. think everyone asking, right, will I replace our jobs and all of that? Right. I see tremendous opportunities of growth and new business and new revenues using AI. see my friends that used to, you know, take months to have ⁓ developed, develop social media content or marketing and

PR videos, it takes like minutes now. There's a lot of places you can actually hire online to kind of pay by the job ⁓ using a lot of those things, AI content and videos creation. There is AI education. There's a lot of people kind of writing books and educate people about it. There's just a lot of, you needed to learn four years of coding in order to get a job. Well, now you don't.

but you do need to, I would say if you don't wanna be replaced, if you will, I don't like this word, but you need to learn how to work with AI because your job can be better by doing AI. For example, marketing, if you used to sell something for 50K, take you three months, maybe now you can break the market and sell it, take you two hours and you can sell it by 5K. Again, I don't know the business models. I'm just saying there is a lot of opportunities out there. I see real estate.

You

can just do simulations and ⁓ kind of targeting the right people to sell the houses right. Again, I'm just talking to my friends and kind of understand from their perspective. Fashion, I already see, ⁓ which is actually exciting for me as well as a woman that interested in fashion, is kind of simulation of sending my picture and seeing how that look might look on me or look for me online, like in my range of pride.

**Adam [45:23]:**
What the dress is, the air.

**Karin [45:26]:**
where can I buy that or even hair and makeup. We're kind of moving on from the subject but I would say that and I do see that we will just manage more AI ⁓ versus just kind of continuing to be those task oriented humans if you will.

**Joe [45:37]:**
Thank

**Adam [45:49]:**
I heard a rumor that a

certain podcast host is looking to get rid of his co-host by replacing them with an AI agent. I don't know if that's true, but...

**Karin [45:58]:**
His name is Adam?

**Joe [45:59]:**
Uh, uh, no,

no, that podcast host doesn't want to replace his cohost on air, but he does need to automate the whole podcast production because his cohost doesn't do any of it. So it is.

**Karin [46:10]:**
Yeah, I think that's a place you can use AI definitely.

**Adam [46:13]:**
Wow, I feel

like, you, who are you talking about, Joe?

**Joe [46:17]:**
It's just something I heard somewhere. No, really, I am... We already... A little behind the scenes, not that it's that exotic, but we already use lot of AI to do lot of the editing and produce the show and stuff. But I mean, I want to automate as much as we can, really do it all. Because a lot of it really is tedious, repetitive and all. And whenever I see these things, I'm like, yeah, we can get an AI to do this now.

**Karin [46:29]:**
Yeah, absolutely.

Of course.

**Adam [46:44]:**
because a certain person is busy going to Milan all

the time. That's what I'm saying.

**Joe [46:49]:**
Hey, I bring the laptop with the official sticker. Well, you can't see it on camera, but yeah, you know, I'm always, I'm always working on the show. Always. Anyway.

**Adam [46:55]:**
Yep. So I know you are.

So there's no doubt in my mind, AI is going to change the market. But this is no different from like 30, 40 years ago when people were like, yeah, the computers are going to replace humans. Certain aspects of it. But then things evolve. You learn, you adapt. And then little by little, as that technology grows, people do find jobs.

**Joe [47:08]:**
you

**Karin [47:17]:**
That's a crit.

can do.

**Adam [47:25]:**
So

yeah, I get it like, you know people were first like ⁓ farming we don't want to use machinery We want to use humans and then machinery came and then machinery has improved things and has improved costs Not everything is always positive. But for the most part There's a positive part because you're allowed to expand your operations beyond what you normally would do And if you know how to utilize it correctly, you know, you can do more but less But it's not always you know, but some people obviously don't adapt don't change.

**Karin [47:32]:**
Thank

Correct.

Yeah.

**Adam [47:54]:**
Look, I don't want to lose my job to AI, but there's always a possibility.

**Karin [47:55]:**
Right, right.

Yeah, and I think you put it, yeah.

**Joe [47:58]:**
Yeah, because they're never going

to replace drone pilots with AI, so you're safe.

**Karin [48:03]:**
Yes. I think you put it very nicely. That's usually where I explain to people. I think that's a very great example to look at the internet back in the days. That's just the evolution of it. Look at now, the internet has online stores that today would not be as successful if it was only physical stores. For example, there is education, is communities, full degree you can do online. There's just tons of

**Adam [48:04]:**
⁓ my god.

**Karin [48:33]:**
of positiveness, was then the jobs of web developing and marketing of your web. And there's just a lot of those kind of things ⁓ that help those businesses. Unfortunately, yes, with every evolution, there will be some kind of jobs that will have to eventually kind of gradually ⁓ cease to exist. I'm not saying right now, right? Like it will take some years, but eventually, yes, more robotics will take you. Look at the robots.

⁓

I'm hoping to buy one of those AI robots that Elon Musk is developing, Optimus. Yeah, I see him like literally doing dishes and cleaning the house and obviously we're not talking about the scary part of that, but I'm just saying eventually in your home, I think in every household we will have a lot of those AIs, whether it's a robot or meta glasses or your phones.

**Adam [49:09]:**
the boston dynamics boston dynamics

**Joe [49:12]:**
I've

already...

**Karin [49:32]:**
It will be as Zuckerberg called it, right? He's trying to make a super intelligent ⁓ one AI, right? It will be your assistant seeing everything you see, analyze that, helping you in everything, ⁓ good or bad. But if that's the case, we need cybersecurity even more. We need to secure your privacy, your identity.

**Adam [49:56]:**
So this is a conversation we had in my class the other day and we're talking about AI and the growth of AI and then the the powerful conversation was about whether AI can ⁓ Have consciousness and then people like no way got to be human this and that and everything but They also said that nobody would ever go to the moon. They also said that we never have planes so You never know. Maybe we're gonna have a certain level of consciousness. I think

You know, and especially with with bio computers, computers that use proteins, computers that, know, that can kind of sort of morph a little bit into brains. But you don't know what's going to happen. But we do know that I'm looking for Sarah Connor. I'm sorry. Terminator.

**Joe [50:43]:**
All right,

now we're getting into philosophy and film reference. So all right, that kind of brings us to last call then as we get to the end, God, before we start getting really weird.

**Adam [50:49]:**
⁓ sorry with that!

**Karin [50:50]:**
Hahaha

**Adam [50:53]:**
Well, let's toast to Sarah Connor.

Terminator.

**Karin [50:56]:**
I'm not sure if I want to but okay

**Joe [50:59]:**
One of the great

female action stars, actually.

But in any case, Karin, as a parting thought, all kidding aside, as security professionals, we do have to defend against this stuff. I mean, what would you suggest that people focus on and spend some time on? Just learn. Besides calling Sygnia for help, just, I mean, looking into the agentic stuff, where do you see a lot of value?

**Adam [51:19]:**
Call Karin at Sygnia.

**Karin [51:23]:**
Exactly. Yes.

**Joe [51:31]:**
that people really need to

**Karin [51:33]:**
Yeah, so I think, again, to just summarize what we kind of touched upon during this conversation, ⁓ it will start with some kind of strategy just to understand the use cases, right? Just understand what are the use cases, where does it make sense to start, just start somewhere. ⁓ Have a conversation ⁓ with global leads, with leaders. It's not just a security thing. AI is not anymore just security or just

technology aspect is to sit with legal and privacy and data scientists and engineers. It's a collective ⁓ effort I think so it will really need to just understand from strategy perspective. Again going back to the governance that's important. Adoption and integration. ⁓

process as well and yeah start from there. think we have of course, of course you can you know also I think we published few articles about it but we're talking a little bit about the governance, about threat framework modeling. I think I know you mentioned governance is boring so if you want to really get into the you know the which I understand no one wants to pay for that or to actually do that but it's it's highly important is you know every executive order of AI or

**Joe [52:45]:**
That's that's.

**Karin [52:54]:**
framework talked about how important it is to be transparent and responsible AI and trust AI. So it is, I think this is key. ⁓ And threat framework is very, very important. That's the actually really more depth and detail around those AIs and kind of how you're looking at each of them to implement. yeah, and just be aware. Educate your organization. Educate your, of course, your employees. Have a policy.

of what we allow, what we don't allow, what you can use and what not and make them understand the risks for the organization. yeah, I think it's exciting. Just go with the wave as well. I think it's a lot of great opportunities as well.

**Joe [53:43]:**
Yes it is and it's a tough challenge and like I said, ⁓ you're not stressed out enough, you'll be stressed out more by this. I would never encourage drinking but like I said, the wine in Italy is really cheap and good. No, we never say that.

**Adam [53:59]:**
So you're not worried about

our autonomous robot that has AI that can fly, that's a drone, that also has EDR, an MDR built into it that can inject, I'm sorry.

**Karin [54:07]:**
go to Italy, bring wine

**Joe [54:13]:**
You know, we're getting into some crazy stuff, but you know what, Karin? I've said it before on the show and elsewhere. I'm with you. I want the optimists or whatever it is to do the laundry, take out the garbage, ⁓ know, sweep the patio so I can hang out, know, mow the lawn. ⁓ I can't wait for that.

**Karin [54:25]:**
cycling.

**Adam [54:31]:**
Do my dissertation? ⁓ no, I can't do that.

**Karin [54:31]:**
Yeah, so we can actually have,

**Joe [54:33]:**
Do it.

**Karin [54:33]:**
like the idea is that you may have more time instead of repetitive tasks, so we have more time to decision making, strategic thinking, quality of life. Again, I know there is a huge part beside that and a lot of people will start with the AI go wrong and the future, and like Adam's mentioned as well, but ⁓ I tend to be excited versus scared.

And that's the future, that's the future.

**Adam [55:05]:**
I'm excited because if I know how to use it and I know how to sell it, I know how to make money.

**Karin [55:11]:**
Yes, exactly.

**Joe [55:12]:**
That's right. And I

can also tell you, ⁓ you need to have some, realistic. It's like, I'm not getting ⁓ the robot haircut until it's like at least version 25, you know?

**Karin [55:22]:**
Right, right. I saw a

robot in China, in a surgery, in the eye, and I'm like, I'm not letting any robot yet there with any knives around me. Yes.

**Adam [55:25]:**
We'll set it up.

**Joe [55:29]:**
⁓ I don't know about that. Yeah. Yeah. Yeah.

**Adam [55:34]:**
Was that a dig at me, Joe, about the haircut thing?

**Joe [55:39]:**
No, you should be even, should be just as nervous. mean, you know, do you want some buggy AI shaving your head? I don't think so.

**Karin [55:50]:**
We're not trusting them yet. So trust is important with AI, that's for sure.

**Joe [55:52]:**
Not quite, it's gonna take a while. That's

right. All right, well, yes, Karin, thank you so much for joining.

**Adam [55:57]:**
You've been amazing, Karin. Thank you.

**Karin [55:58]:**
Thank you guys. You've been great

and wonderful and thank you for a lovely conversation. I'm always here to talk about AI. As you see, it's my favorite topic to AI, to the robots of the future.

**Adam [56:08]:**
Who AI?

**Joe [56:09]:**
That's right to AI and to you, Karin. That's right. It's going to be a great

future and it's going to be exciting.

It's even more exciting if you give us your comments on what you think about AI. What do you want more? Put it in the comments. Do you want the AI robot for your house or do you want an AI ransomware defender? That's a good question.

**Adam [56:31]:**
Or do you want Adam

to come by your house and fly the drone and do surveillance for AI?

**Karin [56:35]:**
Do you want a digital twin of yourself that can do your actual work and podcasts? I'm trying to build my own A.I. digital twin and do podcasts with it. Let's see when that happens. Definitely will have you there. ⁓ This will take time. The fact that I'm trying versus actual, it's just an idea out there. So maybe we can all work on that together. ⁓

**Adam [56:38]:**
⁓ yeah.

**Joe [56:50]:**
Karen, you're trying to my profession and my side hustle. Wow, that's rough, you know?

**Adam [56:54]:**
No way.

Notice how Karin

snuck that right in there at the end. Joe, Security Cocktail Hour is now owned by Karen.

**Joe [57:05]:**
Seriously.

All right, there we go. Your digital twin, okay. Well, you know, have your digital twin talk to my digital twin and we'll figure it all out. All right. Well, thanks again, Karen. And thanks everyone

**Karin [57:09]:**
by my digital twin but exactly exactly thank you everyone bye

**Adam [57:17]:**
Thank you guys.

**Joe [57:20]:**
for listening. Take care.

