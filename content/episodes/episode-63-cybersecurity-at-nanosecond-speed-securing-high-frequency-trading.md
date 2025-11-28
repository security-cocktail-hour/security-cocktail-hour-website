---
title: "Cybersecurity at Nanosecond Speed | Securing High Frequency Trading"
date: 2025-11-17
draft: false
guest: "Jatin Mannepalli"
category: "General"
duration: "59:59"
image: "/images/episodes/episode-063.jpg"
description: "Jatin Mannepalli explores high-frequency trading security challenges, incident response, and custom hardware with Joe and Adam."
platforms:
  youtube: "https://youtu.be/LFvm6aHARak"
  spotify: "https://open.spotify.com/episode/2nanQ96nOpxOihgrXTnSxZ?si=lODg2Y9cRe2iSmsG9srohw"
  apple: "https://podcasts.apple.com/us/podcast/security-cocktail-hour/id1679376200?i=1000737112271"
  amazon: "https://music.amazon.com/podcasts/d11e431a-f7b1-4bb0-8671-024afce9ade6/episodes/08ce4c4e-6f40-403b-9102-c59b59df37bd/security-cocktail-hour-cybersecurity-at-nanosecond-speed-securing-high-frequency-trading"
guest_bio: "Jatin Mannepalli, Information Security Officer, IMC Trading"
---

In this episode of the Security Cocktail Hour, guest Jatin Mannepalli introduces co-hosts Joe Patti and Adam Roth to the high-speed, high stakes world of high frequency trading (HFT) and its many security challenges. The conversation delves into the intricacies of high frequency trading, the stress of incident response, and the importance of redundancy in connectivity. They discuss the evolution of data transmission methods, the challenges of security in trading environments, and the role of custom hardware. The episode also touches on the current job market in cyber security and the necessity of collaboration among firms to enhance security measures.

## Episode Timestamps

- 00:00 Introduction to the Security Cocktail Hour
- 00:26 Jatin Mannepalli: Experienced InfoSec Officer
- 01:54 Understanding High Frequency Trading
- 03:54 The Speed and Stress of Trading
- 06:36 'This is Security's fault'
- 09:26 Trading Data Transmission: From Fiber to Radio
- 11:59 Securing Data Over Radio
- 19:00 We're Talking Nanoseconds
- 21:31 Custom Hardware and Operation Systems = Security Challenges
- 29:04 Security Information Sharing in High-Frequency Trading Firms
- 38:25 The Reality of Security Breaches and Accountability
- 43:14 The Importance of Controls and Monitoring
- 52:17 The Future of Cybersecurity Jobs and AI Impact
- 59:48 Thanks for Watching!

## Topics Discussed

- Cybersecurity
- Podcast
- Hardware Security
- Software Security
- HFT
- High Frequency Trading

## Full Episode Transcript

Jatin (00:00)
Now we are talking about single digit nanoseconds these days, everything adds up to this.

**Joe [00:06]:**
Welcome to the Security Cocktail Hour. I'm Joe Patti.

**Adam [00:09]:**
And I'm Adam Roth.

**Joe [00:11]:**
Adam, looking good today.

**Adam [00:14]:**
Thank you.

**Joe [00:15]:**
So this is gonna be great. I'm getting back to my roots. We're getting back to the stuff I did back in the day. So this is gonna be fun. If you know what that is, put it in the... Today we have a great guest. We have Jay Mannepalli. Jay, welcome to the show.

Jatin (00:33)
Yeah, honor to be here. Nice to be here, of course.

**Joe [00:38]:**
No, it's great seeing you. So Jay, why don't you tell us a little bit about what you do?

Jatin (00:43)
Yeah, I am basically, I have been in InfoSec for what, close to 10 years now, but a part of it now I'm working for a company called IMC Trading. We are like a high frequency trading firm based out in Chicago. So I'm basically the InfoSec officer basically doing work for IMC Trading. So anything related to trading, anything related to financial markets, anything related to exchanges, that would be us. So on a day-to-day basis, you will probably see me configuring firewalls to configuring, I don't know, identity protection SaaS vendor, or you'll be seeing me working on an AWS service, an AWS account, and trying to figure out how... but my head towards it to figure out how to make things work in AWS or any other kind of cloud service that we use. Yeah, but yeah, before this, I was basically into management consulting, revolving around security, like working with healthcare firms to make sure that they are bringing up their security up to speed. But life just happened and I came into a high frequency trading firm. And life has been amazing so far.

**Adam [01:55]:**
I knew one guy once he, when it was a big thing, I mean, I might, I don't want to take it away from Cisco, but when it was a big thing to be a CCIE and the guy was working on a trading floor and he was working with somebody else and the other guy, unfortunately, what he did was he made a misconfiguration of the firewall that cost or lost 13, 14 seconds of trading. And they literally just walked him out the door after that says you're done. And I'm like, and if I understood correctly, it translated into millions of dollars lost like 14 seconds, high frequency trading.

Jatin (02:33)
Like a second in a trading environment is almost like, let's say, a year of downtime. That's a lot of money. I mean, I was talking to my friend recently about how we try to shorten our time and bring like a low latency as much as possible. And this is where it kind of gets tricky, right? Because when you're introducing like security controls or let's say even firewall, right? It kind of breaks things or it makes things really, really slow. And even like a microsecond of delay can cause like so much of losses. And then you have to kind of figure out what works where and where can you make that trade off.

**Adam [03:12]:**
This is a perfect segue, right? I think, you know, even myself, including, right? We all understand high frequency trading from, you know, from a layman's term, but maybe we should kind of describe that, right? What is high frequency trading? What does that really mean to somebody who's listening to this who wants to understand that?

Jatin (03:31)
I mean, think of us like this. I mean, we are high frequency trading firms as well as market makers, right? So who are we basically at the end of the day? So basically when you go on to your trading platform that you use, let's say Robinhood, or you our app, you go and see, Apple today is trading at $500 or a stock or something, but who decides that it is $500? It's basically firms like us that basically get all this information from exchanges, see what is the trading volume based on the demand that various people are buying and selling and based on that each of these trading firms compete with each other to like see what is the most optimal price can I offer to the person who is trying to buy or sell them and this has to be done at like really, really at lightning speeds. Whichever trading firm offers the most optimal price, the lowest price wins. And I think all these firms like us, Jane Street, Citadel, we often compete with each other to make sure that we are providing the best price while making a fraction of it when somebody is trading on these stocks, if that answers your question.

**Adam [04:47]:**
Thank you. I mean, I think it's not, I mean, obviously, of course I could always use a clarification and understanding because you think you know, but when you deal with somebody like you, then you kind of really know. So thank you.

**Joe [05:00]:**
Yeah, Jay, you're a little understated. I mean, it's like high frequency traders. It's yeah, you know, it's a little fast and we've got to be careful. I mean, this is the big money. This is the serious big money. I mean, like you said, these guys are making fractions of a penny, but you know, millions of times a minute or whatever, or even faster. So this is big money, this is big stress. Like you said, 14 seconds of downtime cost millions of dollars. That's what we're talking about. This is the show.

**Adam [05:31]:**
Yeah, probably tens of millions about hundreds of millions and that's a good segue to Joe, right? So we, so Jay we, we talk often about people that do incident response and the stress beyond incident response. Having to deal with people who've been ransomware, having to deal with the CEOs and everybody else is worried about their files. What is a stressful day look like to you and how come you still have hair on your head?

Jatin (05:54)
Usually on a stressful day, what does it look like? I, I've seen days when people are literally pulling their hair because their trading platforms are not working. And since their trading platforms are not working or there is a downtime between various offices that we have. And we are various offices that we have exchange information in real time. And that has to be like super duper instant. So, and when that happens, are literally, everybody at the end of the day, blame security. They're like, there is something in the middle. I'm sure security did something. And, and there's not just for like trading, but I've seen that happen with various other places as well. So when something breaks and people are like, that must be a security control or that must be somebody from security who must have done that. And then you're literally pulling your hair, trying to understand what these systems were to begin with. Because a lot of times these are super proprietary information or super proprietary systems, right? That you probably haven't seen much before in your previous places. But then you are trying to figure out how is the information flow working, how are radius controls making it work, and who did this change, who probably might not be working anymore, and how do you fix this over a period of time. I remember when we had something called a ransomware, not here, but from previous places. It took us almost like three months to bring everything back online. And it was a nightmare.

**Joe [07:27]:**
Pain.

Jatin (07:28)
Sure that all the systems are cleaned before we bring them online, making sure that we put the right signatures in place. Do we have the right host intrusion protection and prevention system on all these systems that are coming back online? Do they have proper access control? When you're expecting people in the office, is the office Wi-Fi clean? Are you giving them, are there the right controls in place to make sure that there are no worms on the networking map?

**Adam [07:53]:**
So I got my next question, Jay. I'm sorry, I'm a kid in a candy store. So I work for a company and we provided kind of a sort of trading platform, right? And one of the things that I was tasked for as a director of operations was to make sure my connections were diverse. And one of the things I've learned about, even in New York City, but this is 15 years ago at least, even in New York City, you can have 15, 20 different providers, internet providers. But the end of the day, 18 of them might be all going over the same last mile. So my goal was to always ask the provider, what is your last mile? And I would find out, and one of them, a very popular location in New York City, Tenth Avenue we found out that the last mile majority was their copper or their fiber or their circuits, so you might have I don't want to say names of companies, but like I say you had ISP A and ISP B and ISP C all three of them even though there were different providers they went over the last mile which is provider D. So that provider got cut then you lost any of those other providers. So how does somebody like you make sure you have diverse connections to trade without having problems?

**Joe [09:26]:**
Wait, before you answer that, Jay, I gotta give a little more history, because what Adam's talking about is totally right, but it's from like 20 years ago. You know, when a lot of people, and I don't know if you're aware of this, but when a lot of people in trading and the financial markets discovered that, especially, well, obviously in New York, when they discovered that they're, that they didn't have that redundancy, that redundancy that they had were really going through the same fiber, through the same wire or anything. That happened for them on 9-11, which was bad. Yeah, which was, and a lot of people who thought, we're diverse, we're covered, it ended up they weren't. So there was a big change after that. And one of things that was built was there was actually a financial network that was built specifically for a lot of trading and it was fiber. Do you know the term dark fiber? You ever hear that one? Okay, it's kind of, I know it's kind of old, but you know, dark fiber just meant you had your own fiber. You weren't leasing it from anywhere. And it was the only way to be sure that your stuff really wasn't redundant. And that gets to what Adam is saying because the way you've solved it now is really interesting because fiber was the fastest, cleanest thing we had at the time. But how do things look now?

Jatin (10:44)
Yes, actually that is a good segue, right? Because in the past indeed, fiber was the fastest way. It certainly still is in certain contexts. But when you're talking about Earth in general, everybody is fighting for, like you said, Internet service providers, redundancies and whatnot, and something breaks in the middle, and that kind of causes things. But now things have changed in the last few years, or at least since the time I've been here. Now we are talking about something called radio towers. We are here. So the thing is when you are transmitting information or transmitted data from point A to point B, in an ideal world, you put a straight line and that solves the issue. But things are kind of variable here, right?

**Adam [11:17]:**
Yeah. Yeah.

**Joe [11:17]:**
Radio is that crazy they do it radio. Bad.

Jatin (11:34)
When you're traveling from Chicago to let's say Tennessee, it's not a straight line. You will have like tunnels, water bodies, name it. And then you kind of add more turnarounds for this and that reduces the speed. Even though optic fiber gives you what, two thirds of the speed of light. And now that you are kind of going around mountains, water bodies and whatnot, that even reduces the speed. So people were like, yeah, what can we do to reduce this speed? Now people are doing radio towers to make sure that information is just going equally fast. It's not the speed of light, at least it is more reliable these days. It is definitely able to solve a lot of problems that people had in the past.

**Joe [12:20]:**
That is just amazing to me for a couple reasons because, you know, like when I was in learning telecommunications back in the late 80s, you know, they would talk about, a lot of the engineers and all will talk about the old days of when data transmission was done by towers and stuff. And in fact, I live close to Bell Labs here in New Jersey, where they did some of the first tests with like long range radio, but that had been dropped years ago. And they're like, no, you gotta use fiber. Fiber's fast, it's got less latency, just boom. And to hear that to get faster, you've gone back to radio is just wild to me. And there's also the security of it. Own the fiber, it's very secure. I mean, what are you guys doing about security and, you know, over the air?

Jatin (13:06)
I mean, that is a problem with radio towers and radio waves. A lot of times you have to figure out how to encrypt that information because it's not encrypted. And that is a challenge. A lot of people who work within high frequency trading are trying to make that work. How can we add encryption to these? How can we make sure that... I mean, a lot of times I think I've seen with one of my colleagues works for a different company. They mentioned that there were people who were trying to add like jammers in the middle when there was transmission of data. And because of that, they had to, they had like downtime of at least a couple of hours. And that was a huge loss for them. So sorry, were saying.

**Joe [13:41]:**
Yeah.

**Adam [13:48]:**
Yeah, I'm gonna jump in because I get everything you're saying and I've been involved in this, right? I mean, the problem with analog is you can't encrypt analog, but you can use digital over radio waves. But when you use digital over radio waves, there's a level of overhead. Even back after 9-11, I was doing FSO or free space optics. And what I was doing was I was shooting lasers from one building to another building when all the circuits went down because we had our own level, we had a BLEC or building local exchange carrier. And basically for people who don't know what a BLEC is, it's basically you're a telephone company in your building. You have all the infrastructure, you have these 5ESS or these big switches and you can do everything else. Even back then we had DSLAMs or DSL multiplexes. DSL was an old type of service for those who don't know. But these days people with Elon Musk and his own satellite services, it actually makes a really good backup. It might not be as high, you know, as high speed, but there are new alternatives to everything. And that's one of the good things. But as far as going about jamming and signals, we have the same issue with drones. We have the same issue with terrestrial connections into space. Space is one of the biggest domains now that's being pursued. I just went to a show or a conference called the GreyCon at Capital Tech University. And that's the big thing. Everybody's using satellites, thousands and thousands of satellites. And what I heard is even Russia moved their satellite into place and went right in between two satellites to stop the connectivity to satellites orbiting the earth. So now we're in a new domain where people are intercepting or blocking signals in space now.

**Joe [15:46]:**
That's what was interesting because, in the financial markets, we said, we're not going to deal with that. We're just going to have private fiber, you know, so everything's tight. You almost, you can even make a case that you don't need to encrypt it. It's so, it's so private. And, you know, it's hard to disrupt. You got to literally go into a, you know, go into a manhole to go and disrupt it or mess with it. But now you're back out in the air and you're right, I mean it can be disrupted. You got to worry about denial of service at a scale you never had to worry about before. You got to obviously worry about, I mean what about weather? I mean, if you're hundreds of miles, aren't there weather issues with that?

Jatin (16:23)
That could be an issue. I mean, the thing is, when you talk about, when you compare, I think that's a very good analogy that you mentioned here, Adam, that why not use satellites, right? And that's a very good thing to think about. So when you're talking about satellites, you're basically talking to like a satellite that's like miles and miles away. But when you're talking about like these radio towers, right? These are definitely the, not like thousands of miles away, but at least the way their setup is. We at least try to make sure that there is like some level of redundancy happening because at the end of the day, it's about latency. The more you try to reduce the latency, the better. I can definitely not say how much speed it is adding from what I remember because I had a coworker of mine who also was asking me who was, hey, why don't we use satellite or why not use that? Well, technically, yes, that is doable, but that will definitely add at least microseconds. And given that now we are talking about single digit nanoseconds these days, everything adds up to this. And that's why we have like, a lot of these firms have like continuous radio towers, right? Each tower is like at least a few hundred miles away probably. It is not known where they are, but yeah.

**Adam [17:41]:**
Well, that's the funny part Jay, right? Any one of us, I don't care who it is, anybody listening to this, and I hope a lot of people listen to this. I hope the millions of people that are listening to this really enjoy this thing, the millions. But anyway, if you're driving down a street, a main street, anywhere you are in New York City, in Chicago, people tend to look up and go, okay, look at all those towers. Oh no, those are the microwave towers for my cell phones. People don't realize that these landlords are getting ridiculous amounts of money to rent their roof rights to these companies to place their equipment on there. So it might not just be a microwave tower for your cell phone. It might be a tower for a proprietary connection for a corporation that needs to do a long haul connectivity from the end of one borough to another borough because they're doing it. It might be government, people don't realize how much government stuff is out there. And guess what? It's also on top of bridges. The top of bridges is some of the most highly technical locations and people don't realize how much they're watched. Like government law enforcement agencies, they watch that stuff. So yeah, there's a lot of infrastructure going up and people don't realize it. And thank God they don't know.

**Joe [19:01]:**
Well, you-

Jatin (19:03)
But what you said is right though, that having a Starlink satellite or have a satellite that would make us as a security people life much, much easier. You don't have to worry about data in transit or encryption or things like that. And that is everything that is covered. But hey, that's the trade off a lot of these trading firms have to make sometimes as to security or do we make more money.

**Joe [19:32]:**
Alright, so let's get into that because here's why this is interesting. This is kind of the punchline to a lot of this stuff. You've got to do super low latency. You know, low latency stuff's got to get there fast and everything. It's nuts. Huge volumes going very fast. Back when I was doing this, we were shooting for like latencies of like 50 microseconds.

**Adam [19:54]:**
Three milliseconds? I don't know what I'm saying.

**Joe [19:57]:**
And I told that to Jay and he kind of laughed at me. And what do you say you're doing that single digit nanoseconds? Like, but the idea was that because it was so fast, at least by those days, there were a lot of things with security we couldn't do. You just couldn't do it. There was no firewalls, couldn't keep up with it. There were no IDSs. Getting an IDS to keep it up with it was very difficult.

**Adam [20:23]:**
That's always the issue Joe right because as things started moving from hardware to software for firewalls. You know everything was always hardware. It was this chip and that chip and this and that and then firewalls started inspecting the connections for things like malware and ransomware. It wasn't like that in the original. It's like oh, is this TCP? Is this UDP? Is this port 554? Is this port 80? You know things like that, but now it's like we're looking for like needles in the haystack, but here's the fun and I know this doesn't, this is not what Jay does but what Jay does from an infrastructure standpoint is just as important to people performing surgeries when one person is in I don't know Germany and they're doing the surgery in New York. It's got to be low latency. It's gotta be highly redundant. It's got to be nanoseconds because if that person's operating that robot and they lost a nanosecond or two, they might have snipped somebody's artery instead of cutting out that cancerous thing. I mean, I'm not an expert at that, but that's kind of like a very loose way to say it.

Jatin (21:32)
No, no, I think you're right. I think latency indeed is like, it's very critical when it comes to like healthcare, financial market. And it's just becoming more and more thanks to like all this development and like AI and people building like GPU clusters that is becoming more and more of a requirement these days that you try to send all your data that you can into your GPU clusters that you have or if you have anyone to begin with. And actually funny story that you mentioned because you said in the past it was all about hardware. It still is about hardware. People are still sticking to hardware because a lot of times people have to create their own FPGAs. People have to set up their own hardware because without that hardware you cannot like trade on a trade with high frequency, with low latency.

**Joe [22:11]:**
What's up? So you're doing custom-built hardware now in trading? Wow, I didn't have that before. That's wild.

Jatin (22:19)
Yeah, yeah, indeed. I mean a lot of firms do that. Yeah.

**Adam [22:24]:**
I don't know if you know Jay. He doesn't say Jay Jay has about 50 to 100 million dollars in stock in Nvidia and I'm joking. I'm joking.

Jatin (22:35)
If only. But indeed, I mean that's the thing right when you have like custom hardware I think this is something probably you guys have seen it too. So when it comes to custom hardware and now we are talking about like what kind of, what kind of software does these systems have, is this custom built, is it in-house, or who is developing this, what kind of platform are they using, and that kind of creates a whole different kind of forms. If it is in-house, usually we normally consider that as safe, but again, these days with third-party and malicious libraries that is out there. So we never know people who are developers who are using third-party libraries, using their Python or C++ coding they could still be using malicious software and bringing in something on their FPGAs. That could just cause another havoc. I have seen that happen a lot of times with other places where you are bringing in all these third party malware and that is causing a huge set of different problems.

**Joe [23:32]:**
Well, I've experienced that. I mean, there's been a lot of stuff with Python and a lot of other libraries and stuff lately, but, you know, I never thought about it to the point where you're doing so much custom stuff, you know, down to the hardware and all. It's like, even with the tremendous amount of money these firms have, they can't rewrite all the software from the bottom up. I mean, they kind of be using stuff that's out there, right?

Jatin (23:57)
The thing is exactly what you said. These are like, this code was created several years ago and it is still using like libraries, custom libraries that were previously used several years ago. And this was an example that we saw that people often push new versions to these libraries and without knowing some of these versions will have malware on them and it's intentional. Though this code has been around for several years, it is still fine and it's still working, but since it is still using an old library that is causing a different set of problems. Yeah, we kind of have to look at the code, make sure that we have the right set of people who understand this, like static code scanners. And once the code is out there, even when we deploy things onto things like Kubernetes, how does the container images look like? Yeah, it's wild out there.

**Adam [24:50]:**
So supply chain compromises obviously nothing new, right? But like I hear stories, you don't have to be government contractors and the CIA and the NSA, but a lot of these companies, what they do, they obfuscate who they are. And what they do is they say to somebody, we need you to write this kind of code, but they don't say we're like a high frequency, you know, trading platform. They're like, yeah, we need this for this and that. So they obfuscate who they are. They go out to an organization and they get the code written, but meanwhile it's like a third party company that you never heard of. It's no different from like feeding the president. You know, the president has people that go out and shop for his food and these they're the nondescript people and they go into supermarkets. They never go to the same supermarkets in the same amount of time. They go there, they buy the food and then they bring the food back. It's the same thing with some of these companies. They go to different companies. They get code written. Tell them what they want. They don't tell them who it's for or they lie who it's for so this way they can bring the code back not worrying about somebody in Ukraine somebody in India somebody in China that's gonna because a lot of the coding platforms are there and then they bring it back in and then they scrub it and clean it and then they turn around say yeah, it's fine. But they make sure never to really go to the same place twice in the same period of time. Does that sound right? Am I making that up?

Jatin (26:13)
No, no, no, you're right. That has been the case and that is...

**Joe [26:14]:**
Don't tell him he's right all the time. That becomes impossible. I thought you were, but no, okay. Fair enough. Well, I'll tell you, this is really interesting because I had thought, and I guess it's my bias from where I've come from, that some of the biggest challenges you had would be with speed and latency and even monitoring the traffic or being able to see it or control it. But, man, the software issues since you have this custom hardware. Now, I'm not going to ask you what you guys run. That would be unprofessional. I know you won't tell me, but I'm going to guess that besides what people have to deal with now, like if you've got a web application and you're using a lot of Python and they say, oh, the Python's been, there's a compromise in it, or someone got some bad code into Node.js or whatever the hell it is. You've got a lot of stuff to do on your application. But I'm going to guess that you guys are maybe not probably not running custom operating systems, but using really tweaked stuff like versions of Linux or something where if you find out something you have has a problem, it ain't exactly like just getting the patch from the vendor and putting it on. It's way more complicated than that.

Jatin (27:33)
No, no, no. I mean, so let's think of it like this. So when you are having all these FPGAs and that you're building, they need some kind of an operating system to begin with, right? A lot of times, since you're building it yourself, it's not like the vendor is going to give you, or you can just go and purchase it online. Let's have like a Linux operating system on it or something. A lot of times you have to build the firmware yourself. A lot of times these firmware are made out of like C++ because that's the fastest programming. One of the fastest programming there is out there along with C. And you are using all these libraries along with it, right? And that is why a lot of developers, they do is they build this in-house to support these FPGAs to make it just like more faster and more more faster. There's always like new, they try to work on launching like new versions of it. Every now and then and that is also a security risk within itself, right? Okay, you're tweaking a code. Okay, how does it look like now? What kind of issues does it, does it translate into? In an ideal world for a company, let's say a, it would be web server. They launch something new and that causes an introduce a new malware but in high-frequency trading firm what it could mean is you get malware or something it fries your chips basically it has happened it can and basically yeah it could be yeah it overheats.

**Joe [28:57]:**
Fries the chips? Wow.

**Adam [29:01]:**
Because it overheats it, right?

**Joe [29:04]:**
That's wild.

**Adam [29:05]:**
They do that on purpose. They purposely increase the consumption so that the power gets more intense as it gets more intense and it fries it. So let me ask you question, Jay. Do you guys ever feel like, I don't know if we're allowed to even ask this, that you're a target of nation states and other criminal organizations that because they know what's at stake, they can make money off you guys if they were able to get insider information, poison the well, watering hole stuff. Do you guys look out for that?

Jatin (29:43)
I mean, we definitely have to keep up with what is happening out there and thanks to a lot of meetups that happened. So a lot of times what happens is a lot of these trading firms come together, they bring their own security leaders, they sit down together. And I like this that I probably have not seen this anywhere else. And I'm glad that something like this exists for high frequency trading firms. So a lot of like people like me or like other, for other firms, come together and they just kind of share what are the issues that they're seeing, what are the nation threat actors are they seeing in their environment. I think I've seen that happen with other firms. I think I'm not going to name, but there was one specific firm here in Chicago that had a really bad day. They got, basically what happened was there was a new version for a specific library and this version was barely there for like a couple of hours. By the time it was known or the person who owned the library deleted it, but for those two hours they had malware on their system. And when that happened, yeah, it was down for like almost six hours or so.

**Joe [30:49]:**
I'm trading systems. That's nightmarish.

**Adam [30:56]:**
Do you guys use ISAC or no?

Jatin (30:58)
Yes, yes, we do.

**Adam [31:00]:**
Yeah, I think it's a fair question to ask. I don't think that's proprietary. You know, when I went to this Capital Tech, Greycon, I saw the most amazing thing I've ever seen. There was a space ISAC, but the space ISAC had a real command and control center. They had people staffed what looked like NASA. It could have met... No, it was not for show.

**Joe [31:23]:**
Those are always for show. Those are fake. Come on. You know that. Lots of vendors have that. And usually everyone's like in a closet and that's the real one.

**Adam [31:27]:**
No it was not for show. By the way, that person might be a guest student, so be nice.

Jatin (31:34)
I mean, you're right. I usually, I think for us, it is FSISAC, Financial Service ISAC. So I think we have, from what I think I've seen this with my previous workplace, which was also a financial industry. I think they do a good job of like sharing information. But when I say, and I think that's the limit of it. They share information, you talk to them and they give their own insights. That's okay, we are seeing this for these kinds of financial institutions. So you should do X, Y and Z. And they'll probably bring some of their customers just to get an idea. But when I say like high frequency trading firm, right? These are like a little bit more knitted community. It shouldn't be like this, but I guess since the business...

**Adam [32:16]:**
It should be though. Jay, when and why?

**Joe [32:18]:**
You don't fit.

**Adam [32:18]:**
Because you guys are trusted, you're like family. And even though you might be competing with each other, it also behooves you to communicate. When Joe and I worked together, Jay, right? We did LS-ISAC, though Joe didn't give me really access to it. He wasn't a nice guy when I worked for him. But that being said, the LS-ISAC would give us information. These threats, these IPs, ingest this, do that. And it was really good for us because we learned a lot from people, even though they might be competitors. It's funny, right? It's like frenemies. We might be competing with each other for work, but those are the attorneys. But the people like us, the security people, we have to work together because we don't work together, divided, we're nothing. Together, we conquer. So good stuff.

Jatin (33:06)
No, no, no, you're good. You're right. So the way I mean, the good thing is these days with a lot of controls that are out there like the intrusion detection prevention systems, they kind of get these feeds. If you mention it to them that, hey, we are a high frequency trading firm or we are like a healthcare, they kind of try to source this information directly from ISAC. I've seen that happen quite a lot of times. So you get this kind of information as to what should be blocked and what shouldn't be right away. But yeah, I mean, when you talk to these kind of coordinated communities, you kind of understand what kind of security strategy they have, because they also face the similar challenge. Okay, speed versus security, what do we choose in a situation like this? I'm sure you saw this, person A. What do you have, what have you done when you had something of a similar situation? Or let's say you had a breach, how did you come up or what kind of authorities did you have to notify? Because that is required by a lot of states, a lot of countries these days, depending on where you're operating. So that kind of interaction with them often makes life so, so much easier. It definitely does.

**Joe [34:20]:**
Yeah, well, we've got to give a little context too. Adam was talking about the LS-ISAC, the Legal Services ISAC. Information Sharing and Analysis Center. That's what it's about, sharing and analysis. The LS-ISAC was a really small one and it was fairly new and was just getting spun up. But the FS-ISAC has been around for a really long time and it's probably the biggest and definitely one of the most active. I'll tell you, there are summits. I think there are twice a year. Have you ever been to one of them? They're a lot of fun. They're a lot of fun.

**Adam [34:55]:**
It's like, make it rain.

Jatin (34:57)
Ha ha.

**Joe [34:58]:**
But there is a tremendous amount of sharing and they offer a lot of resources. And it sounds like from what you're saying, there's even more sharing going on than there was in the past, because it used to be when I was in financial services, people in security were pretty tight lipped, just weren't allowed to talk a lot with our peers or competitors.

**Adam [35:16]:**
I think...

Jatin (35:19)
I think given that these days every system is interconnected, I mean with these third party breaches that are happening, supply chain, I think sharing this information is becoming more of a need than being luxury that was in the past. A very good example was this CrowdStrike that happened. It wasn't a breach, but it was definitely a downtime issue, right? Just because somebody pushed code that they were not supposed to. And that caused a whole different set of havoc for a lot of trading firms as well. I mean, it kind of wrecked a lot of people's lives as well. People were stuck in airports, people were stuck anywhere in the world. But here, when it came to high frequency trading firm, a lot of our competitors were down, including us to a certain extent. And we were trying to nail this to understand how are other people doing it? How are you kind of dealing with this and talking to them constantly? Figuring this out with them based on like incident response as we are bringing systems back online because a lot of trading stuff can happen on Windows machines as well. Those are the ones that were mostly impacted during this downtime.

**Adam [36:24]:**
Yeah, I want to say this though, I want to be very fair. So much has happened over the last 10 years in our lives, whether there's a LastPass compromise or a CrowdStrike, you know, bricking of machines. People are so quick to judge. Everybody's a Monday morning quarterback. I'm probably gonna get threatened after this, you know, we gotta be fair. You know, it's not a matter of if, it's a matter of when. Every company is probably gonna suffer some kind of outage. AWS, Microsoft, Amazon, Google, they're all gonna suffer outages. This is just the world we live in. The expectation of five nines, which is literally five minutes of downtime the whole entire year, it's a hard thing to maintain. It's like running through a highway while cars are going 100 miles an hour. I give a lot of credit to a lot of these companies. I wanna give credit, maybe others won't, but you know, this is, excuse my language, the shit that keeps you up at night. You know, somebody like you that has to make sure that a trader doesn't come to you, I shouldn't even say this, with something in a threatening manner because you put three seconds of outage and they lost $62 million. This is a hard world where we're very, very critical of people, very critical when they can't do their soduku or their Tetris or their online gaming or you know, everyone's worried about privacy and you know and about protecting kids. Yes, we should all be and we can always do a better job. But it's, but if unless you're on the inside seeing what's going on, everyone wants you to do more things with less money. They want you to be a hundred percent perfect, never have an issue, never go to the bathroom, never get lunch, and never, and always answer every single phone call in the middle of the night. Alright, rant off.

Jatin (38:25)
Yeah, I mean, I've seen that happen where you kind of do something. I was with one of the previous financial firms I was with, you make a small change that causes a downtime of five minutes at best and the person was just let go that very day. And all they were trying to do was just updating the firewall or something, right? It isn't supposed to be super duper, sometimes when you have the right HA pair in place, but on this day for this person, it was just a really bad day that didn't work for them.

**Joe [39:01]:**
Yeah, but I've seen cases where people have gotten fired. In fact, I know of some notable and one famous one where the person wasn't so much fired for making a mistake or getting something wrong. He was fired for doing something outside of process. And during the hours, he wasn't supposed to do it. And that's one that's hard to defend. It's like when you get pulled over for speeding. You know you're going fast, you know you're breaking the law, but everyone does it. Well, just tell the judge, you know?

**Adam [39:32]:**
But you know, Joe, something happened to me once where I was doing something for a company and it wasn't with you, don't worry. And we were working on some circuits and I knew that the circuit blipped and I knew it came back up. What I didn't know was they were monitoring the IP addresses of the both sides, the physical IP addresses. What I didn't know, I took over the organization not more than two months after that, that they weren't monitoring and they were using Microsoft Operations Manager. Do you remember that MOM? All right. So then it became another name, but what I didn't know was that there was an encapsulation, a tunnel that had RFC 1918 or private IP addresses and that tunnel even though the physical connection came right back up the tunnel didn't and they weren't monitoring the data passing. That's like going into a candy store and seeing the 6532 pieces of candy. Who's counting every single piece of candy? Who has the time to literally go in and review the thousands and thousands and thousands of things that are being monitored? You have to hope that the people before you were doing the right job and yes, it behooves you and you have a duty to act to make sure everything's being monitored. But how do you know the absence of a delta of something that was never there? You know something that's there, that's down, you don't know that something was never monitored.

**Joe [41:11]:**
Well, that's why you've got to test. You've got to try these scenarios and see what happens, and you get surprises.

**Adam [41:15]:**
So if you're there two months and you're trying to fix all the wrongs, you can't fix every wrong that fast. I'm protecting myself. I'm an advocate for myself, but go ahead.

**Joe [41:22]:**
Well, if you're there too much and the thing is a disaster, that's not, you know.

Jatin (41:27)
I mean...

**Adam [41:28]:**
Well, Jay, let me not get you in trouble. But let me ask you a question. Do you think you're 100% sure of everything that's being monitored and managed perfectly?

Jatin (41:37)
I mean, that's like asking, you know, is everything perfect in the world? No. So.

**Joe [41:42]:**
Yeah, what are you, a White House reporter or something? I mean, that's an impossible question, dude. Come on!

**Adam [41:45]:**
I'm making a point we...

Jatin (41:45)
Hahahaha!

**Adam [41:49]:**
Do the best we have the integrity to do everything we think is right, but we can't be perfect. We're not we're not robots. There's no way to know every single thing. Yes, we go in and we test and we do down and we bring things back up. Sometimes we don't even have the capability of testing every single aspect of something all at the same time. So you might say, let's drop this tunnel, let's bring this tunnel up. Let's drop this hardware, bring the hardware up. Are you gonna drop everything to do fail? Accept, don't get me wrong, Netflix is pretty good with the Chaos Monkey. I mean, they're really good, but go ahead.

Jatin (42:29)
Let me give you a story of one of the breaches that I saw when it came to one of my clients that I was working with. So what happened was I used to work with a person. So what happened was they were like a developer, but also it was a very small organization. So everybody was doing basically everything. So the IT guy was basically just one person or maybe like two at best. So what was a big business? It was definitely doing some millions of transactions and whatnot. So what happened was this person, he is a developer, was using, he had every kind of cool detection system on his computer that was supposed to tell him that everything was working fine and everything is working fine. It did, at the end of the day. But what happened was he didn't have any controls when it came to coding and whatnot. So he actually installed something from a third party library and that kind of introduced the malware on his system. He didn't know about it. Neither did the control on his machine because this was coming from a library. This is not something that he downloaded. It's just basically a code running on a container. So basically, the malware jumped from his container to his machine locally. And afterwards, since he's a domain admin, he has to log into a domain controller. So he connected to a domain controller and the malware got onto that domain controller. And given that domain controllers are like really, they replicate each other, right? Every hour or so, depending on the kind of business you operate. This malware basically spread itself on like 10 different domain controllers within a matter of few seconds. And next thing we know, we were getting all these alerts at that time. We were like, there is an alert coming in. There is a malicious PowerShell script that is trying to do something. Okay, what is that? And when everybody connects to a domain controller at the end of the day, when they have to log in into a company system, everybody who was logging in got that malware and they had like a notepad on their laptop saying that, your files are getting encrypted. We were like, what is happening? We then figured out at the end of the day that this was coming from, like something that this person just basically used as a library at the end of the day. So my point being is to your question or to your point that yes, it's hard to keep track of what is happening in this case. And especially if you don't have the right controls in place, you will always miss something. All this and all this and all this, yeah.

**Joe [45:01]:**
Well, I can tell you though, I mean, hearing that story, and you know, I don't mean to beat anyone up or anything, but you know, I don't want to say it was predictable, but...

**Adam [45:01]:**
We can't go ahead, I'm sorry.

**Joe [45:13]:**
I'm not shocked that given the lack of controls there that something happened. I mean, are, you know, sometimes we see things like, you know, it's so subtle, this is tough to find and all these things. And then sometimes we see things where like, you know, where like, this is an accident waiting to happen, you know?

**Adam [45:30]:**
Everybody should have PAM, get it, privilege escalation. You should never log in with the domain. You should never log in as a domain admin. You should always privilege escalate to that domain admin. You should be going through privilege access management. You should be using detection and prevention. There's a million things, but we don't always get that power to purchase those items. Sometimes people, it's about, you know, it's risk versus reward. Look, I'm gonna piss Joe off. Watch this, Jay. I figured one of the best things you can have in place was to have a packet inspection. North, south, east, west.

**Joe [46:06]:**
Oh God. It's too bad we're not drinking because that's a shot right there. If Adam mentions PISM or packet capture, yeah.

**Adam [46:17]:**
So what I wanted to do was we were working for I don't want to say the organization and they had very proprietary intellectual property and the problem is yeah, there's also encapsulation and encryption, but you want to know north-south. North-south is always the best way to go coming in but you also want to know east-west. So for those who don't know, north-south is coming from your higher level internet services down to your organization. East-west is going from one network to another network within your own domain, your own network. So if you're an organization or corporation, east-west is going from your legal computers maybe to your human resource computers going to your financial computers, but let me just tell you this Jay, I'm a novice. I'm not smart. We were doing a red team somewhere and a purple team and what I did was I used a service account and I logged on to the red team's computer and I took their files and these guys are 50 times smarter than I am, these people are 50 times smarter than me. But the end of the day you can't have eyes on everything. They saw a service account. They didn't know type one versus type two who's sitting there watching that on your laptop. I took their files. I took their hashes. I might have changed some things. Somebody might have gotten mad at me. I've said this before I had to go put their files back in place. They didn't know it was me. Someone told them was me whatever but the point I'm making is you don't have to be smart but you can't blame these people that might be 50 times better than you because you can't have every single control in place. It's impossible. It's like watching surveillance cameras. You feel the hundreds of surveillance cameras in front of you. You're not gonna capture everything.

**Joe [48:05]:**
Okay.

Jatin (48:06)
Ha!

**Joe [48:07]:**
Okay, for the record, Adam was kind of cheating because he was one of the reasons they weren't looking for this was because he wasn't supposed to be doing that.

**Adam [48:16]:**
Maybe they should have been looking, Joe.

Jatin (48:16)
You.

**Joe [48:17]:**
But I should have been looking anyway. That's right.

**Adam [48:19]:**
Let me tell you something, every network is a hostile network. If you're doing reconnaissance, you gotta worry about somebody coming after you.

Jatin (48:27)
I know I think that that's that's a good example. I mean you can't have controls indeed, but at least what you can do is have visibility right of some sort a very good example visibility... No, no, so this this this situation that I told you right where I saw...

**Joe [48:28]:**
That's a nice...

**Adam [48:36]:**
What did you say? Civility? I think civility, actually. I don't have any civility either. I'm not civil with anybody. Go ahead. Sorry, sorry, Jake.

Jatin (48:53)
Ransomware happening right in front of my eyes just because of the library. The client never had a SIM to begin with. So when, and that made just things really, really worse. Basically at that time that they were only relying on what the intrusion detection prevention system would give them. And that was basically just watching it as a watcher, not doing anything else. And since everything was just falling apart, we had to just go into these systems, look at these systems manually because they were storing them to certain extent. A lot of times, what was worse was a lot of times what the backup team was doing was they were backing up these systems on the system itself. So when the ransomware hit, how do we recover the system? Well, the backup is on the system. Okay, how do you get that? I don't know. So basically that's why when this kind of things happen it takes months. For us it took three months because we barely could see backups anywhere that yeah.

**Joe [49:52]:**
Well, look, this is a tough job. Security is tough. And you can find a lot of these subtle things, and it is difficult to sort it out. But you don't have to be a genius to know you shouldn't be, putting the backups on the same server you're backing up. My God, seriously.

**Adam [50:10]:**
But but but but Joe but Joe we've had these comments.

Jatin (50:11)
Ha!

**Adam [50:14]:**
So these are all tabletop exercises. It's hot, cold, cold, warm, warm, hot, hot, cold, warm, hot, warm. So when you're backing up, are you backing up electronically? Are you backing up with traditional tapes and stuff? If you're backing up electronically, the systems are connected. What are you gonna do, air gap the system, you know, throw like, you know, shoot the signal one way, you know asymmetrically? You're always gonna have some kind of vulnerability. And this is what I've seen over and over again. People are like, oh shit, our warm site is corrupted because it moved, that malware moved to where we were backing everything up once a week to over there. I mean, at least back in the old days with that, you know, those tapes, there was always a good tape somewhere because not every tape got infected because it was never there, but as you start backing up online, as you start backing up via, you know, some kind of connectivity, there always runs the risk that that malware will get there. Even in air gap systems, malware gets into systems. How can they, yeah, even in air gap systems, you're getting screwed. Somebody's moving from a Bluetooth phone to somebody else's system. Oh shit, let's hop on here. Let's hop on there, you know?

**Joe [51:23]:**
Yeah, you can still do that. That's true. I know, but you gotta try. Like I say, some of these things are subtle, they're complicated, but some of these things are gimmies too.

**Adam [51:37]:**
I might say don't try, Joe, but... Joe, I'm not saying give up, I'm just saying that if you throw tens of millions to hundreds of millions of dollars, even our own government gets it wrong sometimes, not because they're horrible, it's because there's so many moving parts. People move from traditional internet into secured networks because they buried themselves all the way through and they found the tunnel, they looked for the light. There it is, you know? It's hard, it's such a hard world, we're all interconnected. My brain is probably connected to my computer now.

Jatin (52:17)
Ha ha ha.

**Joe [52:19]:**
Well, Adam, you've been such a bundle of joy today that I'm going to ask Jay to give us the last word as we get to the end here. No, don't say but, but and say something that's going to send me to the bar.

**Adam [52:30]:**
I guarantee if I ask Jay for a job, he's never hiring me, so it's good.

Jatin (52:34)
Hahaha! I mean, the way to look at this is, again, at the end of the day, it's a breach that is going to happen. And when that happens, and you were talking about this, that companies are trying to do things for free or like at the minimal cost as much as they can. But that significantly changes when there is a breach. The client I was working for, the security budget like became 10x the year after. Get all the controls that you can, get Splunk, get everything that you can that is the most expensive.

**Adam [53:10]:**
Micro segmentation, IoT, DLP, you know, IDS.

**Joe [53:15]:**
Yeah, we've talked about that before saying like, you know, sometimes after a company gets breached, they become world class, you know, because they just go out and get everything, you never know.

Jatin (53:23)
Yes.

**Adam [53:26]:**
Jay, check this out, Jay. You're on LinkedIn a lot, right? Okay. What's one of the things that you see on LinkedIn that's really disturbing? I'm trying to lead you to this. I'm gonna say it. I see so many people begging for jobs. There's no cyber security jobs out there. How can there be no cyber security jobs out there when when people, when these places are getting breached and everything else? And we as one thing that's really upsetting and I'm a sucker. I've seen more than one person online saying, you see me for the last eight months. Look at my feed. I've been looking for a job. I'm getting, I'm getting, I'm becoming, I'm becoming homeless. Can people send me 20, $30? Cause I, I'm going to get, um, I'm, I'm, I'm going to get thrown out of my home. How is that possible that all these cyber security people, some people that really came from really good companies can't get jobs. So the point I'm making is we talk about all these companies putting in these security practices in place. But nobody's hiring.

Jatin (54:32)
No, that is true. And thanks to all these vendors out there that are like, I mean, I think that's kind of an innovation in a way if you think about it, that are introducing quote unquote AI or machine learning onto their tooling. There is a bit of a misconception that, hey, if I get this tool that has this new AI capabilities that is going to just cut down the workforce that I have by like 10% or I think we have seen that happen with a lot of firms out there. And the big brunt of it is something that a lot of graduates are coming out these days. Because since you basically don't have much of an experience, and since a lot of these firms are automatically doing some level of entry-level job because of these new AI capabilities, people are not able to get a job because of that. And I think I've seen that happen more and more with security these days. I mean, yes, indeed. I mean, I've seen a lot of even certification based organizations like ISC2 and whatnot who say, yes, there is a lot of demand for security. But if I were to indeed, like you said, go out and actually see LinkedIn, yeah, it breaks my heart. It kind of makes me scared as well. Okay, so say if I have to look for a job tomorrow, how is that going to look like for me? Even though I can basically do a lot of these stuff, lot of people are talking about these days, GPU clusters, AI and whatnot, I've been part of that, but still it's scary out there.

**Joe [55:59]:**
Wow, well, both of you seem determined to take us out on a downer here. So I'm gonna have to, oh God, yeah. What's in that? So I'm gonna have to take matters into my own hands and say, at least, Jay, you mentioned AI a couple times and that's great for the SEO. So thank you so much. That's good for us, you know, that's awesome.

**Adam [56:04]:**
Why do you think I finished this show? I'm just gonna say that, the SEO. Yeah.

**Joe [56:22]:**
And we can come back and do a whole other show on that. Yeah, the hiring situation is crazy.

Jatin (56:26)
A lot of these high frequency trading firms are hiring a lot. So I'm sure they might be hiring a lot of security folks as well because these days markets are super volatile. So that's what happens when the markets are super volatile. High frequency trading firms make a lot of money because everybody is buying, everybody is selling and based on that, they're generating revenue on top of that. So even though I say that the future is bleak, at least some part of it isn't fully bleak. So if there is revenue, that means there will be hiring and there will be fully equipped teams.

**Adam [56:55]:**
Yeah. I don't think, I don't think it's-

**Joe [57:01]:**
And we'll be posting Jay's email address on our website so you can contact him with your resume.

Jatin (57:05)
Ahahaha!

**Adam [57:07]:**
I don't think it's that bleak, you know, I mean, I know I said a lot of things, guys. I said a lot of things and I know there's a lot going on, but yes, you know, as people might have known, we've done a lot of shows with recruiters and we speak to recruiters a lot. And the recruiters are saying that yes, that we're on our third year of hiring issues. But I do think there's a light at the end of the tunnel. I do think there's a lot of move to technology that we weren't doing before. Ironically my son, you know, he had this mining rig and I said, let me go sell the money. It actually got delivered today. We no longer do mining because of proof of stake versus proof of work. But what we didn't know is that these mining rigs are being converted into AI farms. So people are taking the same Nvidia even the older cards like 3090s and stuff and they're using these Nvidia cards to create their own AI. So yes while something's traditionally I have not been hiring for there is still a lot of AI to learn and even though they say AI are taking jobs. There's still a lot of people I mean the height of the big people that were hiring for AI I think was Mark Zuckerberg. He was paying them like sports salaries, you know 30 million five years, you know sign-on bonus. I know we're selected but but but but everybody wants to become that.

**Joe [58:24]:**
Well, well, not everyone. You're talking about like five or six guys, you know, getting that kind of money.

**Adam [58:32]:**
That major league baseball player, that NFL football player. So I'm saying you could still have that. You couldn't do that 10 years ago, Joe. You couldn't be paid like a sports player. But nowadays you can. So my point I'm making is there is some positivity there. Become a division one sports person in AI and then moving to the big leagues.

**Joe [58:54]:**
There you go. All right, well we're gonna have to leave it at that before you say anything depressing again. But Jay, thanks so much for joining. This did not go where I thought it was gonna go with everything that's going on. So it shows you what I know. So thanks for coming on and giving us some new info.

Jatin (59:12)
Yeah, the pleasure is all mine. Thanks for having me. I'm really glad I was able to talk to you guys, really able to share what I know. I'm sure you guys definitely know still a lot more, but yeah, at least I'm glad I'm able to share the ins and outs of like how high frequency trading firms work and at least based on my experiences with breaches and whatnot, I'm able to share and at least share my two cents that a lot of people may not have seen before. So I'm glad and I'm thankful. Appreciate that.

**Joe [59:41]:**
Thank you for coming on and thanks everyone for watching and we love our audience. Right Adam?

**Adam [59:46]:**
Like, subscribe, comment.

---

**Related Blog Posts**:
- [When Nanoseconds Matter: Security for Performance-Critical Environments](/blog/when-nanoseconds-matter/)
- [Why Security Always Gets Blamed (And How to Change That)](/blog/why-security-always-gets-blamed/)
