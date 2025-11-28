---
title: "The New Rules of Cyber Incident Response | New attacks, new response"
date: 2025-04-11
draft: false
guest: "Lisa Landau and Tim Shipp"
category: "Incident Response"
duration: "51:44"
image: "/images/episodes/episode-053.png"
description: "ThreatLight experts Lisa Landau and Tim Shipp on how incident response has evolved and why the old playbook no longer works."
platforms:
  youtube: "https://youtu.be/xilVhM0ZInU"
  spotify: "https://open.spotify.com/episode/2vGLhgkE4enl4J6I2s2UG9?si=8df7b0473f8642e8"
  apple: "https://podcasts.apple.com/us/podcast/security-cocktail-hour/id1679376200?i=1000703154455"
  amazon: "https://music.amazon.com/podcasts/d11e431a-f7b1-4bb0-8671-024afce9ade6/security-cocktail-hour"
guest_bio: "Lisa Landau and Tim Shipp, CEO/ThreatLight, CTO/ThreatLight"
seo_title: "New Rules of Cyber Incident Response | Lisa Landau & Tim Shipp"
---

In this episode of Security Cocktail Hour, we go deep into the high-stakes world of modern cyber incident response (IR) with Lisa Landau and Tim Shipp of ThreatLight—two top-tier experts redefining how breaches are handled today.  Discover how IR has evolved—and why the old playbook no longer works.

## Episode Highlights

### Listen Now

Tune in to hear our discussion on the new rules of cyber incident response (IR).

## Key Takeaways

Why speed is everything in breach response
* Why incident response isn’t about flying on-site anymore
* How top teams manage the intense stress of IR
* Why cybercriminals operate like businesses—and how to outsmart them
* Why tools alone aren’t enough—and what your team really needs

## Resources Mentioned

ThreatLight: https://www.threatlight.com

## Full Transcript

**Joe [00:02]:** Okay, Lisa, so you have been in cyber for a while and your background is actually a little unique compared to a lot of the other people we often hang out with, right?

**Lisa [00:14]:** I guess, define, unique.

**Joe [00:16]:** Well, mean, well, unique in that you're an Israeli cybersecurity person who is not from 8200. Seems like everyone we know is from 8200.

**Lisa [00:26]:** It's true.

**Adam [00:26]:** You...

**Lisa [00:28]:**
Yeah, a lot of them, it's a very, very big unit with a lot of people in it, but yeah, I am not from it. Although, yeah, I am from military intelligence and it's not, like we said, all the Israelis have been somewhere, so it's not that interesting, but it is just relevant to the story because my shift of industries from what I was doing before cyber into cyber kind of was a bit of

closure for me personally and what I wanted to do and what I missed from those good old days. kind of getting into the cybersecurity industry was something that kind of had its sentiments for me and not just a job. Yeah, and then originally I was already in Japan through another company, so I basically helped them start jumpstart Japan and

building it out, building out all the security services, the SOC, and it expanded into advanced services, which in time became IR as well. Some advisory consulting took the role globally from out of Japan. was kind of to sidetrack from that a little bit. That was a bit of a glass ceiling I personally had to break because I was told that, well, first of all, being a woman in a managerial position and especially in Japan is like,

**Adam [01:49]:** Thank you.

**Joe [01:49]:** No.

**Lisa [01:57]:** Something very unusual, but also I was told very clearly by my American management that nobody from Japan will ever manage globally and that was something we changed very quickly. So it was something to work through. It wasn't easy. It was a challenge, but it happened. So I'm very happy about that. Yeah, basically kind of did the security services globally, realized that I really like that aspect of the professional service, the human aspect of the cyber...

**Adam [02:09]:** Good for you.

**Joe [02:10]:** Yes, well done.

**Lisa [02:26]:** And then in the last two, three years, one of the many things I was doing, one of the gigs was to entirely rebuild the instant response practice, which is where Tim and I kind of got together. And I asked him to come and help on the technical hands-on side, which is not my strength. Together we rebuilt the practice. And I think it would make sense that he takes over from there and tell us more, we did build, know, we kind of cracked the code on how to build a dream team and how to modernize incident response and had so much fun that fun was part of it. We decided it deserved a bigger spotlight and eventually went on our own and decided to focus a lot of our efforts on what we believe in and then solving kind of the bigger problems of breaches and not just slapping bandits on them and to kind of to put all the energy and effort into it and to do it right. I think Tim can add a lot more. He has interesting stories about his background.

**Joe [03:47]:** Yeah, Tim, so you're more of the hardcore technical guy, as we say.

**Adam [03:49]:** You...

**Tim [03:54]:**
Yeah, would be fair. I mean, I started my career. mean, technically I was a networking and voiceover IP engineer, went to work for a telephony company. They made PBXs. They were getting a lot of toll fraud. They'd just gone into the IP space over from sort of traditional sort of telephone systems. So started investigating how these companies were getting compromised and how the toll fraud was happening.

**Adam [04:01]:** Oof.

**Tim [04:23]:** Turned out I really good at breaking stuff. So they had to fly me to Japan a few times to sit in room with the engineers and explain how I broke their brand new products. From there, went to a few conferences, found out, turns out you actually get paid for doing this. Off the back of that started my sort of career in doing incident response and pen testing and red teaming. Been building, leading instant response teams for 15 years. I've worked for two defense companies, a couple of security companies, the final one being an EDR provider, which is where Lisa and I met. For my sins, I'm a military reservist specializing in instant response as well. So effectively, I'm part of the UK cyber reserves, although not so much these days because the new business is taking up 110% of my time.

But yeah, incident response is what I do, it's what I enjoy, it's what gets me out bed in the morning. Yeah, been doing it since before. Before cyber was a thing, back when it was good old information assurance.

**Adam [04:39]:** Yeah.

**Adam [05:33]:** Tim and I did a lot of PBX stuff. Did stuff with syrup and skinny and I worked for something called a BLEC (Building Local Exchange Carrier). Not sure if you've ever heard of BLEC? Yeah, because most people haven't but I worked for a company where we building local exchange carrier and we had PBX's in the middle of a gym in the middle of Midtown Manhattan so you would have to walk through a gym, a very affluent gym, go into a closet and there was PBX's in there and risers for 20, 30, 40 floors. So we had to punch down, white, blue, blue, white, white, orange, white, white, green, green, white. And then we'd hook up the PBX's. And I did a lot of small PBX's like Shortail. I did something bad, kind of like in the UK. We set up a VPN site to site. And then we put our Shortail phones in the cages in, I always say it wrong, Park Royal or something like that in UK.

Again, the problem is if you dial 911 while you're in the UK, you would end up calling 911 Public Service Access Point in Long Island. So you're not allowed to do that. You get in trouble for that obviously, but those were the old days.

**Joe [06:48]:** Adam, you're talking about like, you know, closets behind gyms and all this wacky wiring. Sounds like you were like building a boiler room. I mean, Adam, was this legit? I don't know.

**Adam [06:56]:** No, no, no, that's...

**Lisa [06:56]:** Hehe.

**Adam [06:57]:** There are a lot of local exchange carriers put their... They slap their 5ESS switches is what we call them right now. Or the switches in the middle of a... Wherever they can place them. And then their rises go straight up, you know, many floors. So somebody says, I need four phones today. You literally walk over four phones, pop them in, and within about an hour they have four new phones. And back then, we also did DSLAMs. Sorry, so... I'm dating myself DSL, know, multiplexers, oh my god, those good old days. Alright, back to IR, sorry.

**Tim [07:29]:** Yep.

**Joe [07:34]:**
Well, Tim, you know, we've said before, you we've talked to other people in IR and it seems like it's a field where, you know, it's so intense. It's, well, both on the technical and the people side, it's very intense. It's very stressful. It's all this stuff that it seems like a lot of the people, you know, to get into it, you got to love it. You got to be into it. You know, if you're lukewarm and if you're not crazy, you'll go nuts. And gee, it sounds like you not only do it.

full-time 100 percent but then you know even your reserve duty you don't look for a break you're doing it there too wow

**Tim [08:06]:**
Yeah, I mean, things have changed since COVID. mean, you go back six years. I was on a plane once a month to God knows where. I had a bag packed and it was always on a Friday. Call would come in. I'd be making my way down to Heathrow Airport while someone was booking me a flight. But you would potentially be sleeping in a server room or very little sleep until the job was done.

**Adam [08:14]:**
Oof.

you

**Tim [08:32]:**
Things

have changed, things have modernized now. The vast majority of what we do is remote with implementations of automation and AI and everything else. It's taken some of the low hanging fruit. So it's not the 40-hour days that it used to be, but it's still an emergency to that customer. It's still the most important thing in their life at that moment in time. So yeah, you can't half-ass it.

**Adam [09:01]:**
I have a, both of us, we have a friend of ours that was former 8200 working for an incident response company that was spun off by a lot of those people from 8200 and he would tell us stories like, I can't even think for five, six days, like he would be like, we have an adversary, we're handling it, um, because I needed to de-stress, I can't even be by, I would, he would disappear for two, three days, we wouldn't talk to anybody.

And we realized that there's a lot of, ⁓ like critical incident stress management, the same type of stress that you would have if you were a first responder. And, and we understand that. And ironically, when I, I, I, I worked for Joe and we definitely dealt with your EDR company, but that's another story. But, ⁓ at one point when we were doing purple teams with those guys, we were a little bit of a bunch of, ⁓ wise asses. We called our team 8199.

And we did a t-shirt that said 8199 greater than symbol 8200 So we really went to piss them off and we did so much I got reprimanded multiple times because even though I was the blue team I kept on thinking I was the red team Yeah, I'm sorry. I know for the audience red team is the attackers blue teams are the defenders We're supposed to see how good we are for our listeners

**Lisa [10:06]:**
Yeah.

**Joe [10:18]:**
We're good defenders.

**Lisa [10:21]:**
Yeah.

**Adam [10:29]:**
I did bad things, I did adversarial things as a blue team person, I went on their laptops as service accounts, I screwed up their hashes, I did a lot of bad things, I was a bad boy, sorry.

**Lisa [10:41]:**
That's okay, think it's fair to add that the team and blue team is also part of our world and even though we're focused on incident response today, we see it as part of one whole, so we definitely dab into all of them.

**Joe [10:42]:**
Yeah, we're like, you know.

**Tim [10:57]:**
Yeah,

**Adam [10:58]:**
It's

amazing stuff.

**Tim [10:59]:**
you can't defend effectively unless you know what the adversary is doing. So, you know, all of our guys are all dual-hatted. know, when they're not doing IR, they're doing red teaming. But not at the same time, because that's the one thing you can do during a purple team exercise that you can't do during a real incident. You are very much limited to defending, which is a hard bit, arguably.

**Lisa [11:02]:**
how to. Yeah.

Not for the same customer.

**Joe [11:25]:**
Yes,

it is very hard and you know it's even harder when you know you get these very expensive consultants in they put in this whole program we're trying to up our game track like you say the defenders need to learn and we learn against real attackers. Now what does Adam do? He starts like trolling them from day one. I'm like

**Adam [11:43]:**
But you know, in my defense, these guys recommended products. We use products that were already installed. We were, I was listening, I was watching their screens from the day they started looking at everything they were doing and they never knew that that application that they recommended that deception technology was watching all their hashes and all every computer they were on and I was taunting them and they're like, how do you know this? I'm like,

You guys are former like 8200 you guys are like red team figure it out, and I got yelled at by Joe

**Lisa [12:14]:**
or you.

**Joe [12:20]:**
Well, actually, that's a good question. I mean, do you see, you know, a of the ransomware, a lot of these attacks are business now. I know that you're going to respond against. Do you see people, I mean, are the days of the clever hackers and all the people, know, taunting the defenders or messing with them, do you see any of that or is it all just business? They're in, they're doing their job and you got to get them out and that's it.

**Tim [12:47]:**
It's definitely a business and it's the sort of ransomware as a service model. So you've got these, you've got the young budding people who are coming in and typically the ransomware threat actors who are going to actually deliver the payload at the end aren't the people who compromise that system. there's freelancers if you like who are going out scanning the internet, looking for exploits and when they get a compromise, they do that reconnaissance stage to understand

the value of the target they have. And then they will post that on whatever dark web forum and say, Hey, I have got this, you know, this, hospital in X state. Yeah. It's going to cost you $20,000 for access. Um, and it's sold on and sold on until, you know, so, know, then a, proper, a larger, more established threat actor group will then take over and, and, and exploit them. You know, I mean, there are, mean, that is one model, you know, that

A lot of it does vary, ultimately you're right. This is a business. It's not personal. It's, and it's very, very indiscriminate. A lot of people think that an APT is going to be what finishes their company or that's what they're defending against. Reality is it's probably going to be a web shell on a server that you've not patched for two years or a VPN vulnerability that's going to allow an attacker in and it's going to be ransomware that gives you that bad day.

**Adam [13:48]:**
Thanks.

you

You bring up a good point Tim, and Lisa, Joe and I had these conversations many times where we've had old legacy servers that we couldn't get rid of it and we'd beg the company to put the money in there and they're like figuring it out and we would use micro segmentation and put in whatever we could to limit the access to that OS that's been sunset. And for those who are listening, basically what we're talking about is old servers no longer have updates.

And we can't do anything about them, but they need to stay in place and you know Every once in a while the blue moon a threat Intel company would you know that we would use would say hey Just let you know it's out there. Somebody's talking about a law firm on the dark web in Midtown Manhattan That's merger acquisition Just make sure it's not you. I'm like,

**Joe [15:04]:**
That's what we start freaking out. He that's us, us, that's us.

**Adam [15:08]:**
and we were sitting there spinning, spinning, spinning, spinning, spinning and you know, you're constantly in a battle and I know you guys know that because people are constantly calling you saying what do we do? People really get that anxiety. One example really quick is my kid told me that one of the guys that works for me, he got one of those exploitation emails and he was flipping out and I'm like listen, relax. He goes asking for a certain amount of Bitcoin. I go take the text.

**Lisa [15:08]:**
Ahem.

**Adam [15:37]:**
Don't first of all don't answer it. you answer it, I'm gonna beat the living crap out of you. Take the text, put it into a browser, and see how many times that comes up. You're not, you're not special. So, I'm sorry.

**Joe [15:50]:**
Well, actually, with it becoming more routine, mean, you know, some of the, I guess some of the tropes or some of the old school things we've had that, you know, people even though it was said, it's like, you have the technical people, then you have all the business people or the CIO and all the heads. They're in a conference room and they're freaking out. I mean, is that still happening? I mean, at the business level too, or has it become, I know, people are more numb to it or they're like, yeah, this is part of doing business. I mean, what's the stress level there these days.

**Tim [16:22]:**
It really depends on the company and the area they're in. If it's a bank and they can't process transactions and they're losing a million dollars an hour, then it's a lot more urgent than a manufacturing company that can shut the internet, continue to function whilst you fight the fire. It's a sliding scale. Sorry, Lisa, I thought you were going to say something then.

**Lisa [16:46]:**
I think the initial reaction would be this, like Joe described for everyone, because you need to... you don't understand in the first moment what's happening, right? You don't understand if you can still function or not, or if it's something that's spreading or not. maybe at stage two, those who are more tolerant would be, would be, okay, we shut this down, you go work, you investigate while we're still operating. But I think all the... I don't think I've ever...

dealt with a customer who had a breach that didn't have a sense of urgency about them or a sense of stress about them. It wouldn't be natural. You know, they're all very grateful in the end and everybody, you know, like takes all their stress out on you during the initial moment. So yeah, I don't think there's there was anyone who rolled in and said, I understand that I needed an incident response, but I'm totally chill about it. I'm yet to meet that person. Correct me if I'm wrong. Yeah.

**Joe [17:43]:**
I don't know about totally chill, but you know.

**Lisa [17:46]:**
Yeah.

**Adam [17:47]:**
I'll tell you this, right? So what,

you know, when Joe was the head of our cybersecurity program, one of the things that that former Israeli security company did was instilled in us constantly about playbooks and being prepared and tabletop exercises. The more prepared you are, the better you are. And I can use two analogies in two different ways. One,

I like to go in the ring and I like the box. And if you really have that sense of confidence, it doesn't mean that you could beat the crap out of somebody, but you have that sense of confidence. You're going to go in the ring being very calm. You know it's adversarial. You know the person wants to take your head off or maybe hit you. But at the same time, you're to be calm moving around. And the funny part about the whole incident response is it's no different from being, I'm an EMT for only about eight years. I was in an 911 system in New York.

Nobody ever said, oh my God, my father's having a heart attack. I'm so happy to see you. How's everything? coffee? They're not there to welcome you happily. They're like, oh my God, please come in here. What can you do? Help me. Everyone's going to be in a sense of disarray and stress. But a good company that comes in will instill confidence in the client.

**Lisa [18:53]:**
Exactly.

**Adam [19:12]:**
And my wife hates me when I say stuff like this. you know, I never say everything's gonna be okay, because you can never say that. But what I will say is, we will do the very best we can do to restore, you know, your applications and your network to as quick as possible. Because I'll never tell somebody as an EMT, don't worry, everything's gonna be fine, relax, we're here. You can't say that.

**Tim [19:36]:**
No.

**Lisa [19:36]:**
You're absolutely right.

yeah, you know, like...

It's a very good point about the company that comes in is gonna help you and instill that sense of calm. And that's part of our slogans where we say how we're gonna bring the calm into the chaos of the moment. And you've mentioned that other company already several times and I have a few things to say about them and their practices, but I don't know if this is the right time. And I know that Tim will have a lot to add on it, so I'll just say something brief.

He'll expand but on one hand I think it's very good that they made you practice a lot and train you because you know Theories are good, know papers in a drawer are not very helpful When when something real happens on the other hand Playbooks come with a caveat. They they can only prepare you for a very Prescribed scenario which a breach is not going to be and you need to be

**Adam [20:35]:**
Correct.

**Lisa [20:40]:**
flexible and you need to be the EMT, the firefighter, battle tested to know what to do, I will hand it over to Tim because I know he wants to say something about it.

**Tim [20:51]:**
No,

I think you covered a lot of the points as well. mean, I ex-military boxer, I use the same sort of analogies where you've got to be comfortable with the ropes on your back. The first time you're doing this, can't be for real. know, tabletop exercises absolutely have their place. Purple team exercises absolutely have their place. Playbooks, to an extent, as Lisa said, they're only as good as that particular scenario.

What we tend to find is, know, is companies will do the playbooks. They'll do all of the exercises, the tabletops. They'll send their guys on SANS courses. But when it actually happens, it's all very different. And then there's this sort of incident paralysis where everybody just stands there waiting for somebody to do something. it's sort of those first sort of 48 hours, sort of the...

the most critical during that incident. And what we tend to find is it's always a Friday. It's always a Friday. you know, or a public holiday, you know, the customer, you yeah, yeah. And it's by design. It's absolutely by design. That threat actor wants to have as much effect as possible over that weekend. They know that customer is going to ring two or three instant response companies. They're going to...

**Lisa [21:57]:**
Republic holiday

**Joe [22:00]:**
They love the long weekends too, right?

**Lisa [22:02]:**
good

long weekends,

**Adam [22:08]:**
Exactly

**Tim [22:15]:**
They're going to pick one, pick two, they're then going to go through all the commercials and legal stuff. They're then going to go home for the weekend. And we see it all the time where we're ready to work. And they wait till Monday when half the machines are encrypted and everything's already on fire. then it's like, we'd like an answer please.

**Joe [22:34]:**
Wait, really?

**Lisa [22:35]:**
One of the most

**Adam [22:36]:**
What?

**Lisa [22:37]:**
painful things to hear from a customer when they understand they have an incident, let's say you speak to them on Saturday or I don't know, on Friday, and they say, great.

let's do a kickoff call on Monday and yeah and you're like starting to rip your hair out like you're losing 48 hours are you serious you're losing 48 hours because it's weekend um like do you it's gonna cost you so much more

**Joe [22:53]:**
you serious?

**Adam [22:54]:**
Yes Joe

here.

**Joe [22:59]:**
I can't

I can't imagine that. I I had always run things where I mean, going back years and years, it's like, well, we used to have a little more slack, but then when ransomware came along with the encryption, like you got to go now, now, now, no matter what. and you know, the thing about the long weekend was it would be like someone hits you on a Friday afternoon before a long weekend. You know, it, slows you down because people are already leaving on vacation, but people will let things.

**Lisa [23:07]:**
They do that.

**Joe [23:34]:**
go until a month and say, no, Are you serious? That's amazing to me. That I hadn't heard before.

**Adam [23:40]:**
So I gotta tell you, like, when I was on call, I could be in the middle of working out. I could be at a family function. I would get a call and I would have to spring into action, you know, cause I would be that first line of defense. The laptop's there. I'm hoping to have wifi. I have a my-fi probably. Everything's charged. I have my go bag. Joey once told me, goes, I need you to leave Wewar now. We'll pay for that training session. And I left.

**Joe [24:09]:**
Yeah. Oh, Adam used to tell me, goes, you know, I missed this alert on the weekend because I was in the shower. I missed it by five minutes. And I'd say, so what's your point?

**Adam [24:09]:**
I had no choice but-

Well, I mean because I didn't I supposed to turn up the shower every three minutes, but that's another story ⁓ but what I'm really getting at is even if a company already has a public relations company their outside cyber attorney Even the incident response company it still takes 48 hours to invoke everybody get everybody in position You might have one company. I know this is you know, I really believe that because Let's just talk about any company

**Lisa [24:42]:**
And it shouldn't.

**Joe [24:44]:**
That's slow.

**Adam [24:50]:**
They might have somebody go to their Tel Aviv office or the UK office or the US office. It'll take them three, four hours to get that one person there. And then still some people are flying in. I know it's different now, COVID changed a lot of things, but still there's a lot of people who want to come on site. They want to do the forensics. They want to use that hard drive. They want to isolate the machine. And people do stupid knee-jerk reactions. my God, there's a threat actor. Pull the plug. They think they pulled the plug, and meanwhile,

They're already there hanging out, having coffee in the middle of your hard drive, siphoning things slowly through a little freaking shell going out to another place. One of our former colleagues told us not only did a company get compromised, they compromised another company and they went through one shell to another shell out the other ISP.

**Tim [25:41]:**
And that is the second biggest problem we find with IR is a lot of when companies are engaged, a lot of companies are still doing the old traditional DFIR where there's a heavy reliance on digital forensics to the point where they are going in and doing disk images. We've had this with a competitor where it takes us, we design the product so I can spin it up from my phone. It takes three minutes to spin up a customer instance. Customer installs the agent. It's doing 50 % of the sort of

low hanging fruit without any human interaction because that customer that sees so wants an answer there and then, you they don't want to wait seven hours to take a disk image after that person, know, so fly a guy to site, seven hours to do a disk image, seven hours to process that image. That's one machine, you know, let's look at every machine all at once and let's, you know, actually give you some tangible information and Intel to work on. But that's the big problem is, you know, the companies like to fly a lot of people to site because it's expensive.

You know, they'll have six guys and have a project manager and they'll all be billing you. They'll all be billing you. It wouldn't surprise me. But, and that's the problem we come up against is, you've already burnt those 48 hours, you know, deciding on a provider. They're then going to fly someone to site. They're then going to start taking disk images and processing disk images and manually going through master file tables with Excel. know, that time is gone.

**Adam [26:45]:**
Yeah, I killed it, I'm joking.

**Lisa [26:47]:**
You can, yeah, can build them.

**Joe [26:48]:**
Okay.

**Tim [27:10]:**
But a lot of customers don't understand that because not all instant response companies are created equal. A lot of companies, exactly. But as a customer, you don't know that until you've had an incident.

**Adam [27:14]:**
They're a lot of legacy.

**Joe [27:22]:**
Well, hopefully you've been preparing to the point where you modernized your program. Yeah, that's not great. And we should probably get into how incident responses change. Tim, like you were saying, used to be the machine gets compromised. we take it offline. We pull a hard drive. You do all this examination. You had to send someone on.

**Lisa [27:24]:**
That's

it's true, but do I-

**Joe [27:42]:**
on site and you multiply that out, it's very expensive. Now the machines tend to have the tools on them where you don't want to take it offline, you want to see what's going on and see what the bad guy is doing. And that's actually now why you can do a lot of the work remote because you're accessing that stuff even if you're in the office kind of remotely anyway, right?

**Tim [28:02]:**
Exactly. mean, if a threat act has got a remote access, we can have remote access. you know, it depends on the point of the incident. You know, if they're doing data exfiltration and you have no idea what's going in or out, then, you you may need to consider pulling the plug. But if you get in there early enough and, you you're actually in there whilst the incident's happening. This is the problem with a lot of EDRs. A lot of solutions out there will detect the ransomware deployment.

So when the ransomware message pops, or the files start getting encrypted, that's when a lot of, you've missed the entire attack. You've missed the initial infection vector. You've missed the escalation of privileges. That guy's potentially been in there a week, two weeks, a month, casing you out, understanding where your critical assets are, understanding where all that critical information is.

**Adam [28:34]:**
to wait a bit.

**Tim [28:53]:**
you're catching it at the tail end. The damage is already done realistically. You've already lost all your data. They've taken what they perceive to be important and you're just catching the encryption. At that point, you're kind of documenting the, you're just documenting the damage. You're not mitigating an incident.

**Joe [29:10]:**
Right, yeah, it seems like with an attack, a lot of people, even in the industry, they think they've heard ransomware. It's like, so my screen pops up or something gets on my machine, the screen pops up and it's blue or whatever color and it says, you're screwed, you're encrypted, give us a bunch of money. And it's not quite that sudden, it takes longer and you can detect that stuff and respond to it, right?

**Tim [29:32]:**
Exactly that. you know,

yeah, you look at a traditional, you know, a traditional company that's got a traditional file server, you know, so they've got, you know, a couple of terabytes of solid state, you know, old schools, solid state disks. That's going to take a week to encrypt, you know, so when you see that initial ransomware message, you haven't lost everything, but, if you're, if you're going to delay for a week whilst you get guys on site and sign all the paperwork and, you the clock started the moment you've got that ransomware message.

**Joe [29:55]:**
Yeah.

**Tim [30:00]:**
And the faster you can react and the faster you can actually understand the attack and mitigate it, you you mightn't even be at that point where you need to consider paying the ransomware message because you've, you've, you understand what's happened, then you've stopped it.

**Adam [30:12]:**
know where police are on the spot but I think she had something to say.

**Lisa [30:17]:**
We've gone past that point a little bit, but yeah, just wanted to say that, yes, incident response has changed or has the potential to change because not all the consulting companies are willing to change the way they're doing it. A lot of people, like we said, are still doing it in a very human, very analog, very traditional way, not very efficient. We're choosing a different way. But also one of the reasons it's very confusing is because for the companies, for the organizations that are suffering from

breaches because their programs and their tool sets and everything are aimed at preventing the attacks and that's what they do all day long. they haven't gone through a lot of breaches and we usually talk about it in a different context, but it's relevant here too. They don't know what an attack looks like. They don't know what an IR looks like. And we've had it a lot and this is kind of conversations I've had with my team a lot is that you need to

try to see it through their eyes, you know what's going on, you know what's going to happen, you know what you're going to do and how. They don't level with them because they haven't had an attack before, they don't know what an incident response looks like. So we need to... it's not something, you know, when everybody buys, you know, antivirus, EDR, XDR, whatever, but incident response is something that has kind of a lot of mystery.

**Adam [31:35]:**
you

**Lisa [31:47]:**
When there is a breach then we'll talk about it. Most people don't even think about it or don't think about what it looks like

**Adam [31:53]:**
That's a

perfect question to to lead into I think, right? So Lisa and Tim, know, one of the things that I've learned is protection in layers. Am I wrong when thinking that an organization, assuming they can afford it, because you guys, right? You guys are not doing Groupon for your IR. know, companies have to have money to invest to bring you in. And there are companies that want help

**Joe [32:16]:**
food.

**Tim [32:18]:**
Mm.

**Adam [32:23]:**
but probably can't afford it. But let's just talk about prevention. As an IR company, do you recommend an EDR and a deception technology and maybe old school or no NAC? Is there a set of tools that an organization should have to prepare themselves for a possible threat?

**Tim [32:46]:**
think everything helps. Everything's a layer in that defense. mean, having an EDR, crucial. Having AV, crucial. But you need to assess your risk depending on the company as well. If your information is valuable to another organization, to another country, then your risk is probably higher. Even ransomware threat actors now, they have access to the same EDRs that you have.

You know, they will have access to other companies that have, you know, the latest version of whatever EDR they test. They test all their implants. A lot of the obfuscation tools they use, you know, they are sold because they, you know, they're there and you can find them online. So, you you have your, brute retail or your Cobalt Strike beacon. You can run it through, through an obfuscation tool, you know, and that obfuscation tool is designed and advertises to bypass EDR.

Um, you know, so, so it's, it's, it is a cat and mouse to that extent. Have offline backups, have offline remote backups and MFA and your, your, your, your 90 % there. Because what we find a lot of the time is, is the customer has lost their data. The only person that has a copy, you know, the only copy is encrypted. They don't know what the attack has taken logs. You know, you know, the, the amount of times we come into a customer and we can't tell, we can't tell them that what's been taken because they don't have sufficient logging.

It's terrifying how many customers are spending hundreds and hundreds of thousands of dollars capturing logs into Splunk or Elastic, but no one's actually sat down and said, you know, are these logs actually useful? You know, can I, you know, can, can, if there was an incident, can an incident responder actually do anything with these? And, know, and that's why we sort of do the instant readiness work where we will come in and actually check, you know, if you were to have an incident, how effective is your tooling going to be?

But I mean, you can't go wrong with having deception technologies, with having EDR, with having antivirus. Everything's a layer, but these are businesses, know, and their business is ransomware and they have access to all of the tools that you have and they do the testing.

**Lisa [34:53]:**
You need to work back from your...

**Joe [34:53]:**
You know, that's interesting, Tim. I never thought about that.

Like you said, they have access to all the tools. I know they have access to the open source. But are you saying that when they go and compromise someone and they have the tools, they actually use that as their test lab to see how their stuff works?

**Tim [35:09]:**
There

is evidence of companies of threat actors who will use one company to test another company's tools. They'll come for us a less valuable company and they'll do their testing there and they use that as their testing ground, proving ground before they go and attack the big fish.

**Adam [35:31]:**
We can see Lisa

**Joe [35:32]:**
TBS.

**Lisa [35:33]:**
I was just going to say that it's not just the tooling. Obviously, tooling has a place, and Tim said it depends on the company and their outcomes or their non-negotiables of what they can't live without in terms of damage, but it's not just the tool set. It's the processes and how these tools are configured and the preparedness, so it's the overall program with the processes and how all the things are tied together.

you

incident response partner inclusive of this because you know those when it does happen those 48 hours or whatever it may be is critical so if you whoever you're with needs to actually be available to you and And not turn you down so like we for example have a way where we're already like pre-positioned We're there before anything happens other people can do it differently There's the traditional retainers whatever it may be whoever you're with make sure they are

actually available and will be there very quickly.

**Adam [36:38]:**
Do you guys I know a lot of incident response companies are now coming out with your own product where they put their own agent on the machines that they could jump into action and maybe get telemetry is that what you guys do to

**Tim [36:51]:**
So we absolutely do. Yes. So we have our own product and we've kind of focused, we absolutely do Windows, but we've kind of focused on the gaps that a lot of other companies have as well. Threat actors know that Windows is very well protected now. Linux, not so much. Mac, not so much. So we're seeing a lot of attacks now that are targeting Linux, targeting ESXi hypervisors because they know

they know that the EDRs and AV don't necessarily put as much time and effort into those. So that's where we focus now. We focus on Kubernetes, we focus on Docker, on Linux, on your critical infrastructure that is a big dark spot for a lot of companies.

**Adam [37:31]:**
Peace.

A certain EDR company, which I won't mention the name, was not very effective with Linux.

**Joe [37:46]:**
A lot of art.

**Lisa [37:47]:**
A lot of, a lot of.

**Tim [37:47]:**
If you're using a seat by seat licensing,

Windows is your background. Windows is what brings in your revenue and what historically for the past 10, 15 years has been, that's user land. That's spear fishing and Trojanized documents and everything. That was what got you into a company. Now it's compromising a VPN concentration. Now it's compromising an internet facing web application, which are probably Linux.

**Adam [38:15]:**
I was kind

of being funny because I know that a lot of organizations use golden images and certain EDRs don't work great on that master golden image and then you end up running into issues when you start spawning new VMs. So I'm alluding to a certain organization you might know. That's where I was getting at.

**Joe [38:17]:**
to the web.

**Tim [38:40]:**
Yeah, the problem with golden images is they're only as good as when they're created as well. it's, unless you're really hot with updating your golden images. Again, the single biggest thing you can do as a customer is patch.

if you want to mitigate a large percentage of threats. It's not fun, it's not sexy, it's not cool, but.

**Adam [39:03]:**
effective. know, but people, and that's the funny thing, right? Everybody wants that golden, that golden tool and that amazing, you know, this will solve everything, just buy this. But at the end of the day, regular hygiene is what really helps to prevent, in my opinion, and I'm not an IR person, but prevents that, that, that, that attack, patching.

**Tim [39:04]:**
Exactly.

**Adam [39:31]:**
Knowing your, knowing what applications you have, making sure that you do get good use cases with your sim. Nothing is 100%. Making sure that you do actually patch your hardware, your firmware. Firmware is a big issue these days. People keep on forgetting that. Everyone talks about patching images, patching images, patching the app, OS's. Your firmware, if it's not up to date, you're running into issues too, because your hardware...

Sometimes it's touching that internet and you're worried about the software. But meanwhile, there's a vulnerability that's been sitting out there since like the caveman days

**Tim [40:11]:**
Absolutely.

**Joe [40:12]:**
So something I wanted to touch on while we still have time. We talked a lot about how, well just talked about how the threats have changed. People are going after the soft spots we get good on. One thing, they go after the stuff we're not so good on. How incident responses changed a lot, going from the old school on site to now doing remote things, trying to catch attacks in progress, all that kind of stuff.

The other big thing that I personally have always associated with incident response, and we touched on it, is stress. Stress not only for the customers, but for the team. It's a tough job with weird hours. It used to be with a lot of travel, maybe not so much anymore, but how is the... And that's one of the reasons I've said before, you gotta love it. You gotta love doing that stuff because it's not easy. How is the stress level these days? Is it...

Getting a little easier, is it getting tougher? Where do things stand? What you think? What's that?

**Adam [41:04]:**
you missed one part Joe before the answer.

Sometimes the client stressed out the IR people too like myself.

**Joe [41:11]:**
Especially you, yes.

**Tim [41:13]:**
This is something Lisa can answer better than me.

**Lisa [41:17]:**
You think? No, I think we can both speak about it. We've both worked in it. We work in it with teams. I think there's a dual aspect to it. And Adam, you did mention this when you were talking about that other IR company and how they said they were working 14 hours and disappear for five, six days. And that's when I wanted to say that we'll...

why? Not that it's not necessary. So the twofold answer to this is on one hand people who go into this profession are usually, like you said, they love it. So loving the stress of it, loving the urgency of it speaks to a certain character of people that enjoy it. They like going into that hyper focus of the investigation and they just can't remove their

hands from it until they get to a certain point because you start having findings, you think you got it, you think you know where it came from, so it's kind of, you know, you're investigating, you're doing your detective work, whatever it is, and it's hard to put it down. And I think, like, in our prep conversation, we told you guys that we once had to threaten, if I may use this word, employee, that we're going to put parental controls on his computer if he's not going to go to sleep at night.

Because for the guys, it's a sense of accomplishment and it really is an accomplishment when they're solving the problem for the customer and solving the investigation. So that's a really, really good thing. But I think with moving to remote, when you used to send a person on site, that's all you got. That's what the customer had. That's what the organization had. And when they were eating their sandwich at lunch or taking a bathroom break or sleeping.

the investigation would stop and everybody's stress and it's you know the old slow human ways so people really did have to put all their efforts everything dependent on that one person or two or however many they sent and they really would disappear and it was very stressful and there were reasons for burnout and for stress. Today with remote there is no reason for that so I think if somebody is working six days straight or eight days two weeks no breaks 14

our days, then we need to raise a question with our management about why. We rely on remote teams, global teams, we put them in a way that 24-7 coverage would be easier without forcing people to work at night, etc. There are ways around it. You can minimize the stress, can minimize the burnout, and can normalize the work as much as possible, obviously within reason, because there certain logical threads to the investigation.

that is hard to interrupt in the middle and hand over to another person. I think sort of if it's starting to kill people or to cause them real mental health issues, then I think we have some questions to ask to their management. And as management, I hold myself responsible to that, ourselves accountable. So yeah, think outside of us who function best when we're

stressed, there are organizational things that we can do in order to give our people a better work-life balance.

**Adam [44:52]:**
If I can add, so Tim you boxed You said you used to box or you did box? So Lisa like I believe when people go into this almost like the ring for boxing with this incident response is a level no one gets into the ring because they say they want to get hit. People get into the ring well I shouldn't say that I like getting hit but people get into the ring because there's a set of there's a level of endorphins there's a level of

**Tim [44:56]:**
Mm-hmm.

**Adam [45:22]:**
Like, it's like, get, do an incident response is like getting the rings, like, it's like being on a drug. When you're in that, when you're in that IR mode and you're getting to something and there's an adversary and you're defending and you're digging into it, you keep on digging, I think. I've never done what you guys did, but you, you want to get to that problem. You want to solve that problem. You, and it's like mano a mano, even though you might have a team with you.

You're still an individual contributor looking into that. And that's how I see the IR. You get hooked on it. You get high on it. You get this endorphins. Your heart's beating. Your blood, it's just everything about it is I want to win the fight. And that's how I see the parallel between boxing and IR. So.

**Lisa [45:59]:** You do.

**Tim [46:11]:** Yeah, exactly that. So I forget to eat during instance. It's very rare that I'm hands on keyboard these days. But it is something and a friend of mine once described it as it's a cyber knife fight. That's all your mind is trained on. You are then reliant on your managers to pull you out of that and to manage that. We have a global team for a reason. We can hand over from the US to Japan. We can hand over to the guys in Europe.

It's, you know, there's a team for a reason. There's no heroes. It doesn't need to be heroes in this. But it's also why we met, why we're insisted on maintaining it, maintaining bench time. You know, it has to be a good split of when you're at the coalface and when you are doing the IR work and then when you're rotated out for that R and R where you will work on development time and just have some time with your thoughts and your family and just taking some time to decompress.

You can't keep going, that's how you burn out and we don't operate that way.

**Joe [47:13]:** Wow, it's great to hear that you're taking that into consideration. That's a really core thing and taking care of people like that, especially in incident response, because I could tell you in my career, maybe it's because I'm a New York guy. That sentiment has not always been there. And even today, that's not there for a lot of places. And we really do, we talked about it before. I do worry that we have a bit of a mental health crisis.

**Lisa [47:30]:** Yeah.

**Joe [47:40]:** In general in society, but also in information security. There is still a lot of burnout and a lot of people who maybe, like you say, lean towards getting too much into it and they need people who are not going to exploit that to teach them how to pull back and not drive themselves nuts and also actively not exploit it, you know.

**Adam [47:58]:** I joke, yeah, everything's adversarial in New York. You go to get a coffee at the coffee cart, it's adversarial. "What do you want?" "What do you mean what I want? I want coffee!" "Why don't you tell me how you want the coffee?" And you get into the whole thing. It takes 15 minutes to get coffee in New York. Everything's adversarial.

**Joe [48:03]:** Ha!

**Lisa [48:14]:** You know...

**Tim [48:17]:** But you can't give 100% all of the time. That gets to a point where it's diminishing returns. If you've been at it for 10 hours, you're no use to anyone. You're sat at the keyboard. You've checked out mentally whether you know it or not. It's better to hand over to a fresh set of eyes, get some rest, and come back tomorrow.

**Adam [48:36]:** That's so true, mental fatigue. People don't realize, people think you have to keep on going. Sometimes the best thing you could ever do is take that 10, 15 minute break, step back, and then you get like this light bulb over your head, like, oh my God, if I stopped, I would have realized that's what's actually happening. And that's almost driving a car with lights and sirens on and getting those blinders on and not realizing there's a car to your left or a car to your right.

**Tim [49:03]:** I solve more problems, more IR problems in my sleep than I do when I'm sat at the keyboard. I'll literally wake up, bolt upright, like "I'm right back, oh my God," and then I have to go downstairs and check it. And yeah, I've lost count how many times that's happened now.

**Joe [49:16]:** Well that's a good trick.

**Tim [49:18]:** It is, yeah, it's literally when you end up working during your, genuinely working during your sleep and you're like having a dream about the job.

**Lisa [49:18]:** Take a nap.

**Adam [49:25]:** I was in a joke. I don't want people to get the wrong thing, but Tim's like, "Oh my God, I just slept four hours. I figured out the answer. Bill client four hours." I'm joking, I'm joking.

**Joe [49:35]:** Well, well, it's actually better.

**Lisa [49:35]:** That's why we don't bill like that. CTO naps.

**Tim [49:35]:** No, that's just...

**Adam [49:38]:** I'm joking, I'm joking!

**Joe [49:40]:** Well, it's better you do it in your sleep, because I do it, I like to go out in the car and drive. That's how I think, which is probably not the safest thing in the world, to be honest.

Now that's great. Well, thank you so much for joining us. We've covered a lot. You know, it's interesting to talk about incident response. The world with it has changed quite a bit. And I guess to a certain extent, you know, we like to talk about the doom and gloom sometimes. What it sounds like it's changed a bit for the better. That maybe we're getting a lot of things down and it's not quite as things aren't the catastrophe that they used to be when this stuff comes up.

**Adam [50:22]:** I know we're gonna edit but Joe, we should get them to tell the name of the companies a couple minutes or yeah...

**Tim [50:22]:** Yeah, it's...

**Joe [50:29]:** Yeah, okay. Anyway, Tim, what are you gonna say?

**Adam [50:33]:** I'm sorry Tim.

**Tim [50:35]:** No, I lost it a little bit now, yeah. I think it's kind of, it's not, you know, it's not having an incident, it's not a dirty word anymore. You know, companies bounce back from it. It's not something that's hidden in a lot of countries. You have to declare that you've had an incident and a lot of companies come out stronger for it. Having had an incident and learned a lot from it and bounced back. So it's good that it's in the spotlight now and it's...

**Adam [50:37]:** Oh my, sorry.

**Tim [51:02]:** Yeah, there are a lot of companies doing it, not necessarily doing it well, but there are also a lot of companies doing it the old fashioned manual way. And that's effectively what led us to found ThreatLight, to build ThreatLight is to do it the more dynamic, much more quicker way of doing it. I know you can rattle this off much quicker than I can, Lisa.

**Lisa [51:24]:** I was going to say manual may mislead people to think that we're fully automated and this is not what we believe in. Obviously this is very deep expert work. We're just modernizing the methodology and we are utilizing the tools and automating whatever can be automated without removing the human expert aspect from it.

We're strong believers in the hybridity and finding that optimal point where the human meets the modern tooling and the automations. And to also make it more affordable, I think, Adam, at some point you mentioned how to hire you, people need to have the budget. Yes, yes, they need to pay us, obviously. This is not something that we, unfortunately, this is not something we can afford to do for free. But we are building it in a way that we...

For example, the way we built the tooling, the architecture, we thought about, let's not collect all the data we're not going to need. That's kind of everything we're doing. We're trying to build it at scale. And the work is done faster. So it does become a lot more affordable. And we want to allow SMBs to be able to afford enterprise level expertise, which is also important because there's a lot of companies that won't take them on. And that is such a shame because they need the same help as everybody else.

**Joe [52:49]:** Okay, well I gotta say, we haven't actually worked together, but if you guys are as good at IR as you are at just seamlessly sliding the plug in, you're good. I wanna work with you. Anyway, for ThreatLight, we'll have a link in the description. Everyone, please check them out. And the rubber ducky, right? That's right.

**Lisa [52:59]:** You... He's had that duck, he's had that duck sat there the whole time. I was like, well, I don't have a place to put mine. So that's my fidget toy that was in my hand the whole time.

**Adam [53:16]:** I was deeply moved when the ducks, like the 10 ducks were looking into the sunset and it's a threat light. It was, I'm not gonna, I don't wanna say this, but I'm gonna say this and I shouldn't be saying this. When I saw your ducks, I had duck envy and I wanted to look at marketing and make ducks that said in the name of our podcast. But Joe stopped me. He took me out of it.

**Tim [53:39]:** Only one duck died in the making of that photo as well.

**Lisa [53:41]:** Yes, it would have been 11 if one of them didn't fly off the roof.

**Adam [53:49]:** Oh my god.

**Tim [53:49]:** I got carried away by a seagull.

**Joe [53:50]:** OUCH

**Adam [53:51]:** Wait wait wait wait...

**Lisa [53:51]:** You...

**Adam [53:53]:** Wait wait wait wait, did it jump off or did you throw it off because it wasn't compliant?

**Lisa [54:00]:** It took flight. It took flight. It decided to explore freedom.

**Tim [54:00]:** It got knocked off, it lost its footing. It took forever to hit the ground.

**Adam [54:07]:** You...

**Joe [54:08]:** Okay, you have a picture of that, right?

**Tim [54:12]:** Mm.

**Lisa [54:12]:** Mental image of that.

**Adam [54:13]:** No, not the picture of the duck falling off. No, not the duck falling off. No, no, they had the picture of the ducks, not the one falling off.

**Joe [54:14]:** I was going to say we could put a link down if you have a picture, but okay. We'll have AI generate it.

**Tim [54:22]:** We've got, yeah...

**Lisa [54:23]:** Yeah, yeah, it's on our LinkedIn. No, not the one falling off. Not the kamikaze duck, just the compliant ones.

**Tim [54:24]:** 10 ducks in a row, I'll send you.

**Joe [54:25]:** Not the one falling off, okay. That would be... Alright. Okay, well...

**Adam [54:28]:** Mental image!

**Joe [54:36]:** Okay, we'll post the non-injured duck picture then, that's cool. We can do that. All right, well Lisa, Tim, thank you so much for joining us. This has been a lot of fun, really important topic. We love talking about it.

**Lisa [54:39]:** Yeah.

**Tim [54:39]:** Excellent. Thank you guys.

**Lisa [54:46]:** Thank you. Thank you so much for having us. It was fun. Thank you. Always fun. Thank you.

**Tim [54:50]:** Well, see you soon.

**Adam [54:50]:** Thank you guys.

**Joe [54:51]:** Adam, always fun. All right, thanks everyone for listening. We'll see you next time.

**Adam [54:54]:** Always fun.