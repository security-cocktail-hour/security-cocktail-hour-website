---
title: "Crypto Kidnappings, Lost Keys, and Million-Dollar Bug Bounties"
date: 2025-09-09
draft: false
guest: "Yevheniia Broshevan"
category: "Cryptocurrency Security"
duration: "01:05:09"
image: "/images/episodes/episode-060.jpg"
description: >-
  Forbes 30 Under 30 cybersecurity expert Yevheniia Broshevan discusses crypto security challenges, bug bounty programs, and the reality that 95% of Bitcoin has been mined while 11-18% is lost forever.
platforms:
  youtube: "https://youtu.be/erF3zC0a1hM"
  spotify: "https://tinyurl.com/4u6myrb8"
  apple: "https://podcasts.apple.com/us/podcast/security-cocktail-hour/id1679376200?i=1000725711707"
  amazon: "https://music.amazon.com/podcasts/d11e431a-f7b1-4bb0-8671-024afce9ade6/security-cocktail-hour"
guest_bio: "Yevheniia Broshevan, CEO/Hacken"
---

Forbes 30 Under 30 cybersecurity expert Yevheniia Broshevan discusses crypto security challenges, bug bounty programs, and the reality that 95% of Bitcoin has been mined while 11-18% is lost forever.

## Episode Highlights

### Listen Now

Tune in to hear our discussion on crypto kidnappings, lost keys, and million-dollar bug bounties.

## Key Takeaways

* Access control issues and private key leakage cause majority of crypto hacks
* Bug bounties in crypto can reach 5-10% of potential losses (millions in payouts)
* Hardware wallets, diversification, and proper key management are essential
* The industry lost $2.5 billion last year, $3 billion this year - trend is accelerating
* Phishing and social engineering remain the weakest links in crypto security

## Full Transcript

**Joe [00:05]:**
Welcome to the Security Cocktail Hour. I'm Joe Patti.

**Adam [00:08]:**
I'm Adam Roth.

**Joe [00:10]:**
Adam, how are you doing today? I see you've got the background. For once, I've got the shirt on and you don't. But you do have the background.

**Adam [00:18]:**
Well, I know sometimes people can't tell us apart, so if I wear this shirt, people will think we're twins.

**Joe [00:24]:**
Yeah, I know. And when you do those cartoons on LinkedIn and in social media, I'm not really that gray, am I?

**Adam [00:30]:**
Well, I use ChatGPT to make me look better and you look worse.

**Joe [00:34]:**
Yeah, I've noticed that. Well, anyway, we have someone who is a lot younger than both of us, actually, but knows a hell of a lot more about a bunch of things than we do.

**Adam [00:45]:**
Take us to show you Joe, where AI is taking over. Yeah, we're out of touch Joe. We might as well just wrap it up with the Florida or something.

**Joe [00:48]:**
We're out of touch.

⁓

Yeah, well, good luck with that. But we have someone who's going to educate all of us on a bunch of stuff. Yevheniia Broshevan. Yev, hi, welcome to the show.

Yev Broshevan (01:04)
Hey, happy to be here. ⁓

**Joe [01:07]:**
No, we're glad you can make it. you know, you're, you're a little sort of famous. You are one of Forbes is 30 under 30, which is like very cool. And, you know, I mean, we talked about this. went, I looked at that and it said, you know, you're in the 30 under 30 and you've been into crypto since 2014 and all. And I said to myself, did you start when you were five? I mean, like, what's the deal?

**Adam [01:36]:**
Shh.

Yev Broshevan (01:38)
No, actually, I started working in crypto since 2014 when I was in second year of my education. I studied cybersecurity, so it was kind of natural, because originally for me crypto was for cryptography rather than for cryptocurrencies. And I know for a lot of people crypto is cryptography. And probably in the circles is also the same, right?

**Adam [02:03]:**
you

**Joe [02:04]:**
Yeah,

that word has changed. That's right. When people say crypto now, they mean cryptocurrency. Cryptography is too hard, I guess. I don't know.

Yev Broshevan (02:12)
Especially when everyone wants to be rich fast with crypto and then just a lot of disappointment and lost money.

**Joe [02:21]:**
Yeah, that's right. you know, know, I'm at cybersecurity will sometimes say, what should I do with cryptocurrency? Should I buy it? And I say, I know security. I don't know currency speculation. You know, those are two different things, but maybe we'll learn it right here. That'd be cool.

Yev Broshevan (02:32)
Yeah, yeah.

**Adam [02:37]:**
It's funny when you say it right Joe I spoke to my friend Peter last night the one that's supposed to come on the show. He said we snubbed him. That's another story and then he says we never got He said we never got back to him. I like be quiet Peter, but we had a whole conversation He's so knowledgeable by XPS (XRP), but then I started saying well, what about your cousin who was an economist? He goes economists know nothing about crypto. They can't do any of that He goes cryptos crypto economy economists as economists. So we have this false

**Joe [02:46]:**
ever snow.

**Adam [03:06]:**
impression that people should know what crypto is and how it relates to currency and money but it's really not true.

Yev Broshevan (03:14)
Yeah, that's true. Because if we look at cryptocurrency, there is two components here. There is part of finance and part of technology. So originally when I started, this was more about the technology itself, right? And when we were like, it was escalating quickly, especially in 2017 with the boom of ICO, initial coin offering, when people were launching their crypto tokens, right? Everyone heard about that. But like in a lot of circles, it's still about speculation, something illegal.

like

paying in crypto for drugs or something else, right? But if you look at the other side of the coin regarding technology, it's a totally different story. But I think media is more attracted to this kind of stories when something went bad rather than like saying about technology and its benefits. So that's why we have this like wrong impressions. And of course, we had so many scam stories in this industry for like last 10 years.

**Adam [04:11]:**
Yeah, and yeah, he was saying he's like Adam he goes what you're not realizing the XPS (XRP) is not only a crypto But it's also ⁓ a protocol and he goes and when when the US because he's speculating that eventually XPS (XRP) will move into ⁓ one of the mechanisms or or vehicles to move money and this will be the ⁓ way that currency is moved a lot easier worldwide in order to

⁓ Resolve some currency issues and some debt so he went into a whole speculation and I sat there and Whatever here I had left to fill out of my head, but the point I guess I'm making is that he you know people don't realize that Crypto is not just not like you're buying a painting you're buying ⁓ a sofa Buying crypto currency is more than just you know purchasing something it's a methodology into ⁓

into one non-repudiation of where that coin sits on the blockchain and on that ledger, and also about how to move currency in large amounts between countries and stuff.

Yev Broshevan (05:24)
Yeah, exactly. you look at the... You you're talking about currencies right now, but if we look at the market of real estate, for example, you probably guys heard about real world assets and tokenization of real world assets. That's exactly what you're referring to. So it's not only about the finance itself, but it's about assets and moving assets globally across countries. ⁓

**Adam [05:38]:**
Yes.

**Joe [05:48]:**
Okay, so you gotta explain that because I could say I'm gonna play the person who doesn't know anything, but I really don't. In fact, I think you'd said we're not supposed to call it crypto anymore. It's digital assets now. So if you have real estate, I mean real estate, at least in English, the word itself is real estate, something real. So how do we tokenize real world stuff? How does that work?

Yev Broshevan (06:01)
Yeah, exactly.

You

Yeah, so the change in the industry happening recently, because before it was kind of non-licensed activities. We had like digital currencies, but the crypto currencies was like for a long time without proper definition in all countries and accepted globally. Even now we can see that it's called different and different jurisdictions. ⁓

For example, in the US it's Digital Assets, in Europe it's Virtual Assets, somewhere else it has different names. But in the end of the day, it's about the like any assets on chain. There is off chain and on chain. And what you're talking about real estate, this is a part of off chain, which is not happening on like any like blockchain protocol. Let's call it like that.

**Joe [07:04]:**
⁓ so off-chain. I think back in the 90s, that's what we used to call the meat space, you know, the real world. Is that what we're calling it now? God, you haven't even heard that. boy. Wow. Now I feel old. Okay.

**Adam [07:11]:**
you

Yev Broshevan (07:11)
Yes. What does it mean? ⁓

**Adam [07:13]:**
you

**Joe [07:20]:**
The meats bit, you know, where we're real people, you know, with flesh and that kind of thing. Not like avatars and stuff. God, wow. Okay. Real life, like IRL. Does anyone still say that? don't know.

Yev Broshevan (07:23)
like in real life.

Okay. Real life.

Yes, exactly. I

have a run.

**Adam [07:37]:**
IRL was like a big term and we were still old when we heard IRL so you know IRL might have been like two generations ago. Joe, I keep reminding myself how old we are Joe. Well, let me just say this. Let me just say this.

**Joe [07:46]:**
Yeah, that's what... I know, god, we're two generations back. boy, okay. I gotta pay attention here. Where

the hell is my money? I'm getting scared. I don't know.

**Adam [07:56]:**
Joe, let's just say

this, AOL, let's talk about our life and history and technology, AOL just retired. If you ever even knows what this is, I'll be surprised, the dial-up modem service.

Yev Broshevan (08:09)
I haven't used it, I heard.

**Adam [08:11]:**
That's how

old we are, Joe. We started using the-

**Joe [08:14]:**
I know. But I

read that and I couldn't believe they still had it because I don't know if you can even buy a modem anymore. mean, God, find it at a junk pile in a show or something. But anyway.

**Adam [08:18]:**
Okay.

So that goes to show you,

we definitely, there's a lot to learn and unfortunately for us, people like Yev, you know, are gonna know 10 times more of the amount of stuff than we will. it's just, we're like kids in the candy store, Joe. We're trying to eat technology and cryptocurrency and you know, AI and it's just too much. That's why I probably need to lose more weight.

**Joe [08:50]:**
Well, okay.

Yev Broshevan (08:50)
You know, it's interesting

to see that how in this specific industry, it's like never enough what you know. Yeah, like I'm pretty sure that like whatever you learned in your university doesn't make sense anymore, right? The speed of technology and cybersecurity of this technology is developing that fast that you need just like literally be up to date every day. And in our sphere and like crypto, it's like literally a couple of hacks every day happening and you're always learning like what was the mistake there, how you can...

How you can prevent this in the future for for our customers? So it's like never-ending story and it's like 24 per 7 for sure

**Joe [09:29]:**
Okay, so now we're getting into what you actually do these days. So hacks against crypto, which is getting your money stolen, basically, if you have money in crypto. I heard the story, and it's been going on for a while. It's the guy who had, I guess this wasn't a theft, but it's the guy who had hundreds of millions of dollars or something on a hard drive and he threw it out by accident.

Yev Broshevan (09:33)
Okay.

**Adam [09:52]:**
Yeah, we're

just talking about that. Yeah. Yes. Yes.

**Joe [09:53]:**
And the guy, I think it's in Britain or something, and he like wants to buy the landfill that he threw it

in and hire people to comb through it. I don't think that's your end of the business doing that, right?

Yev Broshevan (10:03)
I'm sure. We are like on the other part of this chain. ⁓ So what we do at Hacken, we help companies to prevent risks, which comes to application security mostly. So we do penetration testing, audit, source code reviews of all this, like crypto tokens, blockchain protocols, crypto exchanges, wallets.

that you can think about when you say crypto, there is technology behind that, teams and products, and that's what we help them to protect. ⁓

**Adam [10:44]:**
I

definitely got two questions now. Now you're me all excited and everything. So you do these pen tests. One, the first question is, are these pen tests that you're doing, are there any type of legal, legitimate, when I say legitimate, I don't have to take away from what you do, but frameworks that they get certificates or they get certifications, because I don't even know anything about this. I mean, know like the ISO 17799 and all that stuff.

And then the other question I have for you is you ever do a pen test and then find out ⁓ uh-oh because I've seen this before I've heard this before by IRLs in real life that as you're doing these pen tests they found out ⁓ the person really does have a threat actor on there and I don't even know how to phrase this on their network on their blockchain on there whatever it is

Yev Broshevan (11:36)
Yeah, definitely there are different layers of security, right? There is organizational security, security on the policy level, the ones you're referring to. And in our specific industry, we also called it three, I like to call crypto as Web3.

**Joe [11:52]:**
⁓ yeah, Web3,

Yev Broshevan (11:54)
Yeah, we have many names. We have many names

for everything going around. So we don't have like much standards yet, but we have many like working groups that trying to ⁓ do that. Of course, we have some stuff in OVASP, which comes to like traditional web, mobile.

and like crypto stuff. Also we have another ⁓ consortium, it's called Crypto Consortium (CryptoCurrency Certification Consortium) CC4, which works on different standards for key management and they have a cryptocurrency security standard. ⁓

on the console there, like contributing to the standard itself. So this is one of the initiatives. There's like a couple more working on that. Another one called Ethereum Enterprise Alliance, have East Trust, the one connected to smart contract security and smart contract vulnerability and procedures that you need to follow to, you know.

**Adam [12:44]:**
yeah.

Yev Broshevan (12:49)
to prevent the risks. So we don't have still ISO stuff here. It's not also PCI, DSS, nothing connected to that because we have specific type of technology here when it comes to like smart contracts and blockchain protocols and nodes and consensus mechanisms and cryptography between all this stuff inside. So we need to have special checks, special rules, special methodology and tools that we need to go through while we are doing penetration tests.

You can think about that as the small industry and the bigger industry of source code review. There are different types of code, right? And in crypto, we have our special one. So that's what we do.

**Joe [13:34]:**
you

**Adam [13:34]:**
Do you? Go ahead, I'm sorry, John.

**Joe [13:36]:**
Yeah, we should probably give it a little context. We started talking about a lot of things and I'm wondering if someone listening said, OK, we talked about crypto, I don't get this. But then you start talking about things that are very familiar to security people. And we should probably say in case it's not totally obvious, ⁓ all this crypto stuff uses software. It's all computed. It's all based on software. So when you say you're doing a ⁓ pen test, you're actually testing.

⁓ the software that runs this stuff that holds it that implements all these fancy protocols and it's a lot of application security basically and if it's not working right or someone can hack into it you can be in a world of hurt. I mean it is stealing money directly essentially.

Yev Broshevan (14:07)
Yes.

**Adam [14:24]:**
And that's the question I have, like, like, Yev, I'm exactly like Joe, like, I sound like I knew what I was talking about in the beginning, because I heard five minutes from your friend. So I try to impress people at parties as if I know something about it. And then I'm gonna start telling people I know you, Yev. But that being said, you know, it's like really complicated, because we talk about cryptocurrency.

We talk about currency, but what people don't realize, especially me, is that that cryptocurrency has a technology that has a blockchain and that blockchain has a ledger. And that ledger, you can't pull anything out of the middle because then that hash changes, if I understand correctly, as it goes up. And that ledger is also used for formalizing contracts to be signed. So while you have cryptocurrency, you also have a protocol, I guess, if you want to call it, and that protocol follows that chain. And that chain...

You want to make sure nobody is able to manipulate that chain so in such a way that they pull something out of the ledger and keep on changing those hashes, then make it seem like that ledger has not been altered. Does that sound right or am I just off base?

Yev Broshevan (15:25)
Yes, exactly. So what you're referring to, so that's why I mentioned there is like two sides of the coin, right? So we have technology and finance.

**Joe [15:33]:**
By the way, that's good. see

there's two sides of the coin we're talking about. Digital currency. Well done.

Yev Broshevan (15:36)
I have come.

**Adam [15:37]:**
wow, that was a good idea. That's gonna be the-

we're gonna take that and make it a short.

**Joe [15:42]:**
Yeah, that's going to be a sure excellent. Cool. Good idea.

Yev Broshevan (15:45)
Yeah, so when it comes to technology itself, it's definitely about what you just discussed, ⁓ Adam, regarding the protocol and how there is a consensus between this decentralized infrastructure and nodes, how they are communicating securely between each other and how on top of these blockchains, are like smart contracts deployed that operates on this ⁓ protocol itself. So yes, definitely. ⁓

Definitely it's a complex system and technology that we ⁓ do security for.

**Joe [16:21]:**
OK, so that's really important because it is complex. It's complex software that's running all this. You want it to have vulnerabilities and run it correctly. And I think many of us know who've been in security for a while that ⁓ cryptography software in general is one of the most difficult types of software to implement correctly. And it's a lot of math. It's a lot of random number generation and all these things. And mistakes are really common. In fact, you

**Adam [16:44]:**
you

**Joe [16:50]:**
You often tell people when you're in application security, don't do anything with cryptography unless you're an expert. Right. Don't make up your own. Don't think you can be clever. Don't think you're such a good coder you can do it. It's really a specialty. So what are you finding? You've got a unique thing that you actually look at these codes. Are you? And I'm not going to ask you to call out anything. But mean, generally speaking, are you finding the code that you're looking at is?

Yev Broshevan (16:54)
Yeah, exactly. Don't do it from scratch. Don't do

**Adam [17:00]:**
Thank

Yev Broshevan (17:01)
Yeah.

Yeah.

**Joe [17:19]:**
Very good quality. Nothing's perfect, and they hire you to find the mistake. But is it generally good quality, or do you regularly see stuff when you say, my god, I want to put $10 in here? We've got to get controversial. Come on.

**Adam [17:23]:**
But Joe, that's why...

Yev Broshevan (17:28)
you

**Adam [17:31]:**
Yeah, don't answer that yeah, good show. That's why that's why joke. That's why she's turning No, no, no,

no, no, no, wanted to answer it, but don't answer yet That's why you ever stood you under 30 because she catches all this crap This is what they're so so that's the answer to the question first of all But virtue of what you have does and by virtual you have company name She should be wearing a black hoodie with only her eyes showing that's what people are gonna imagine about you have She looks like a sweet woman and everything else

Yev Broshevan (17:43)
You

**Joe [17:43]:**
Yeah, I guess

so.

**Adam [18:00]:**
But Yev is like, pfft, like a piranha, man. She's like going after code, telling people, listen, this is wrong, get your shit together, excuse my language, but that's who Yev is. Okay, I'm sorry, go answer.

Yev Broshevan (18:10)
Yeah, you know, it's like typical typical ⁓ Like how high hackers look like right in the reality, but let's be honest. It's not the case anymore

**Adam [18:22]:**
No, I know.

Yev Broshevan (18:24)
Yeah, and definitely we own the white side of the business. We're ethical hackers and I'm an ethical hacker myself. Even I was certified ethical hacker by E.C. Conceal some time ago. But definitely, so that's what we do. We spot this kind of vulnerabilities ⁓ in the systems and ⁓

Like for eight years we had like over 2000 different clients and I don't know how many lines of code we audited, but definitely a lot. And when it comes to quality, of course, you know, starting in this industry that long time ago, because this industry is relatively new and like everything we built, we built almost from scratch. All the tools, all the standards, methodologies, you know, because...

**Adam [18:49]:**
Oof.

wow.

**Joe [19:07]:**
Because there's nothing there, right? It's all new.

**Adam [19:09]:**
Yeah, right.

Yev Broshevan (19:10)
Exactly. And that's why when you are asking me about the standards, it's hard because like how many years it took to build like security standards.

**Adam [19:17]:**
well I knew

the answer to that I just wanted you to say but yeah two things Joe one yeah let's spend five minutes and interviewers both we're looking for a job right now and number two you have ⁓ I wanted Joe you and I by the time we're done we could be Forbes 100 under 100 when we learn all this stuff I was joking you up about the job but the point I'm making is it's so and I want to say this is say this

**Joe [19:36]:**
Yeah.

**Adam [19:44]:**
but it's such an interesting place to be. And I'm in a class right now and I'm constantly doing things about ethical AI and I realize I know nothing about AI. I mean, I know enough to know I say I know something, but when I speak to people like you and I'm not looking to like butter you up, I realize the plethora of knowledge. It's like someone hiring me to do incident response or do pen testing. I know, I mean, got SANS, I got SANS certifications and certified ethical hacker certifications.

But that doesn't make me an expert. know, hands to keyboard is where it's at. And it seems like you've been doing this since like you're four years old. So all good. I'm not trying to be disrespectful, but you really got a breadth of knowledge for a new technology. It's amazing.

**Joe [20:29]:**
Yeah, what Adam is saying is when it goes to cocktail parties, he's either going to have to learn more or become a better con man like Frank Ivingdale or something, you know?

**Adam [20:35]:**
That's true. That's true. I'm a good comment

now, but yeah.

Yev Broshevan (20:38)
Yeah, definitely. ⁓ And you know that's why this industry is ⁓ moving fast because we need to learn fast on our mistakes to prevent the future stuff. Because if we look at this year's statistics, we lost 3 billion in digital asset space just by now.

And the last year, whole year was around 2.5 billion, think, something like that. So where is the progression? We're not getting better.

**Joe [21:04]:**
Okay. Okay. So,

so how are those losses happening? What are the big real threats? Because I've heard people say, you know, don't leave your crypto wallet on a machine that's on the, on the internet. Uh, you know, so is it bad operational stuff, bad passwords exposing things, or is it, you know, code quality vulnerabilities where

What should you be most worried about if you're going to hold some of this stuff?

Yev Broshevan (21:31)
Yeah, definitely. So we do like a quarterly reports on the losses in the industry and the HAC cases. And the statistics we see is that the majority of hacks and incidents are connected to access control issues. So it's like private key leakage ⁓ as just, you know, ⁓ like losing access to your crypto. So literally the biggest hacks was regarding the private keys and signing transactions like malicious signing of the transactions.

**Joe [22:00]:**
Mm-hmm.

**Adam [22:01]:**
Ooh.

Yev Broshevan (22:01)
So

that's the majority. It comes to operational security, right? So it's not application security. And when you're asking about smart contracts, of course, there are still the chunk of vulnerabilities that leads to this hacks. But honestly, it's still more operational security issues here.

**Joe [22:21]:**
find that so interesting because I've said for years, people have known for years, it's about key management and everything. That's the real threat. People really don't try to beat the encryption or anything. It's too hard. like the old military thing, say, amateurs study tactics and experts study logistics. I've always said with crypto, amateurs study math.

**Adam [22:23]:**
you

you

Yev Broshevan (22:36)
Thanks

for watching!

**Joe [22:48]:**
when they're trying to break it, but experts study operational security and key management. That's really where things go south. So that's still true.

**Adam [22:55]:**
So yeah,

Yev Broshevan (22:57)
Yes, true.

**Adam [22:58]:**
so yeah, check this out. I used to work for Joe and Joe loved when I worked for him. He was like one of the happiest guys in the world. So when I used to work for Joe, you one of the things that we were heavily involved in is that we were talking about ⁓ the whole thing about bring your own key, have your own key, the keys on premise and everything else. And that seems to be somewhat as similar to like, do you really do you really want your key to be on premise?

**Joe [23:02]:**
was the time of my life.

**Adam [23:22]:**
But at the same time, if your key is not on premise, then people have a way to get your key without you knowing. And that goes for everything from blind subpoenas to hackers and everything else. But I'll tell you really quick story. One of my friends, I used to work for the city of New York, nothing to do with technology. And I worked with a law enforcement agent. And he called me up out of nowhere. And I don't normally hear from him, but I love him and everything else. And we're good friends. And he goes, Adam, I have a question for you. Well, my brother-in-law,

he lost all somebody called him up and said to him that he had to do this he was from like i don't want to say the name of the company and he had a login because it was an issue with his account so he logged into something he must have given his password and username out they went into his crypto account and cleared him out so i always look at that layer eight that that vulnerable layer of the person sitting behind the chair as the operational issue and i always say that about everything

You know, like we can, you know, people steal code and people hack code and everything else. But at the end of the day, the most vulnerable people out there are the most vulnerable thing out there is a human layer.

Yev Broshevan (24:29)
Exactly. mean, it's the same in crypto, where I'm not special with it, it's still operated by human. And you know, the amount of phishing and scams in this industry is really, really high. this year is a big topic on phishing through different attachments and downloadable scripts, because...

So as industry growing, we have like more fresh people coming, right? And you know, you need to educate people and cybersecurity awareness is a big topic, you know, especially because if you look at the banks and the crypto industry is different, everything happening right away and there is no central party to cancel this transaction, right? Like it can happen in banks. So you can call to support, right? They might do something with that. In crypto, it's not, when it's gone, it's gone. You cannot do much about that.

**Joe [25:21]:**
Uh-huh.

Yev Broshevan (25:22)
And that's the problem because people are still the

new people coming are still in the like old mindset. But here things work differently, literally like when you own your keys, you own your crypto, right? So it's your responsibility to make sure that you secure like your wallet, your digital wallet. So that's why stuff can can go really, really bad here. And people are still the weakest chain as everywhere.

**Adam [25:49]:**
The irony today is that the whole entire thing about crypto is when you have your own key, that's the most positive part. You own that key. There's nothing on the blockchain. I know people can try to follow you in the blockchain and see where that currency was when they pay ransomware. But at the end of the day, the most positive part of having the cryptocurrency is the vulnerability itself. It's like a two-way thing.

because if you lose your key, it's gone but at the end of the day no one else has your key ever so they can't do anything with it. it's like a catch-22. The whole idea behind that is that there's no centralization but because there's no centralization, there's no way to reverse that transaction.

Yev Broshevan (26:37)
Yeah, exactly. You know, that's why if we look at the total supply, I don't know, Bitcoin or Ethereum or anything else, there is a percentage of the crypto that lost forever. And it's quite significant, like the friend you described. I'm pretty sure we have more and more stories like that.

**Joe [26:56]:**
So there's a, you know, I never thought about this. There's a percentage that's lost forever. So.

Yev Broshevan (27:00)
Yes,

the supply is limited. That's most important. That's why the cost of it is really increasing dramatically because you can't get more. This is out of...

**Joe [27:03]:**
Right.

**Adam [27:12]:**
supply them in.

**Joe [27:12]:**
You know

what that makes me think of? Okay, I know how we're going to make a fortune. We're going to do the Goldfinger attack for crypto. We're going to find a way to like... Have you ever seen Goldfinger? It's a James Bond movie. Okay, all right. So here it is. My era, we watch a lot of James Bond, Menti. So... Adam thinks he's James Bond.

**Adam [27:22]:**
She is in a Goldfinger.

Yev Broshevan (27:32)
I don't know this is, but I don't...

**Adam [27:32]:**
legit well alright really do you know James Bond at all? No

I wish I was but do ever watch James Bond at all yet? Okay this is a very important question and this is going to define our friendship and our relationship here. Who's your favorite James Bond?

Yev Broshevan (27:39)
Yes, of course.

**Joe [27:43]:**
⁓ God.

Yev Broshevan (27:49)
Like old one or new one or what? What we are choosing from?

**Adam [27:51]:**
You pick, your choice.

any James Bond that's ever existed.

**Joe [27:56]:**
All of them.

Except George Lazenby. You forget about him.

Yev Broshevan (28:00)
I'd probably prefer the like later movies.

**Adam [28:03]:**
But

which one do know which are you putting on the spot?

**Joe [28:05]:**
no.

Yev Broshevan (28:06)
I don't have this on top of my mind, the exact names.

**Adam [28:09]:**
Okay,

because I'm a- I- I- I've caused a lot of controversy in places I've worked, and on the internet, where I'm like- everyone's like, Sean Connery. I'm like, no, not Sean Connery. But I love Sean Connery, but since we're talking about James Bond, I wanted to get your feel on who your favorite was. But we can move on. Let's go, Joe. Sorry.

**Joe [28:25]:**
Go ahead, you can say it. You think Daniel Craig is the best. I know. I've heard it a million times and everyone knows it's Sean Connery. So, you know, give it up.

**Adam [28:27]:**
Daniel Craig is the best, we know that! Daniel Craig is the best!

Look, we've gotten into arguments with co-workers and people in higher levels about this. I've started controversial, like, discussions at work over this.

Yev Broshevan (28:43)
sorry, I Googled now, so I definitely love Jane Craig.

**Joe [28:47]:**
gee, thanks. Okay. Well, anyway, getting back to what we were talking about Goldfinger, one of the classic movies, which was with Sean Connery, the true James Bond, by the way. Goldfinger's scam was he owned all this gold, know, owned this huge stockpile. So he said, you know, gold is hard to steal, whatever. So he goes and he says his trick is he's going to go to ⁓ Fort Knox where they've got, you know, the biggest supply of gold in the world.

**Adam [28:57]:**
Okay, okay.

**Joe [29:17]:**
and detonate a nuclear bomb there, not to blow it up, but to make all that gold radioactive. So his gold would be more valuable. I'm thinking someone's going to do the same thing for cryptocurrency, just make a lot of it disappear and then the value of the rest will go up, especially if it's limited supply.

**Adam [29:23]:**
you

you

Yev Broshevan (29:35)
I would want to disappear, for

his crypto to disappear. ⁓

**Joe [29:40]:**
No, but I mean if

you held a lot, I mean if you make someone else's, not your own, if you make the rest disappear, I'm telling you that's gonna be Bond 26. Just wait.

Yev Broshevan (29:45)
Clear. Clear.

**Adam [29:47]:**
So ⁓ listen

to my friend last night, I don't know much about this, he's like, Adam, when the 21th millionth coin from Bitcoin is found, there'll be no more Bitcoin. And that's it. So these algorithms eventually will deplete whatever coins are left. And that's what's gonna happen. And when you lose the key, if you had $10 million in Bitcoins in that key,

That's in the ether. You'll never see it again. You've actually reduced the amount of Bitcoin but increased your value because nobody else has it.

**Joe [30:24]:**
reduced the money supply, you've created deflation or whatever. so...

Yev Broshevan (30:27)
So we have 95

% of total Bitcoin possible issued by now, so we have 95 % left.

**Joe [30:35]:**
How much is it estimated is lost?

Yev Broshevan (30:39)
Let's check how much Bitcoin is lost.

**Joe [30:41]:**
Let's see.

**Adam [30:43]:**
I had like a-

Yev Broshevan (30:43)
uh okay it says uh 11 to 18 percent

**Joe [30:51]:**
11 to 18 % is

**Adam [30:51]:**
Yeah, yes, go.

Yev Broshevan (30:54)
Yeah, it looks like it's familiar in B2C.

**Joe [30:55]:**
Ha!

**Adam [30:58]:**
It's not stolen, it's lost. yeah, lost means like people had it in their Bitcoin wallet. So my friend said to me, Adam goes back in the day when I had Bitcoin, he had like over a hundred coins I think, and he had it when it was less than a dollar each. And he turned in his computer, he goes, Adam, there was no hardware wallets back then or any, he goes, I lost it based on software. It's gone. I don't, I was in a file. He goes, I'll never get it again. I can't cry about it. Now he goes, I'll make my money with XPS. That's what he said. So it's pretty funny.

**Joe [30:59]:**
love.

Yev Broshevan (31:00)
Love.

**Joe [31:28]:**
Okay, so don't lose it. So ⁓ what if you're going to hold it? mean, are the best practices? And I mean, do you even advocate it? is it what's the conventional wisdom? Is it that, yes, you hold it yourself and take care of your keys and everything, which a lot of people can't do, or you're better off letting a service do it and trusting them because you can't even trust yourself? mean, what's the current thinking on that?

Yev Broshevan (31:54)
Yeah,

it's a good question. think diversification is very important here. So a lot of people store their crypto on like their non-custodial wallets or custodial wallets or like crypto exchanges or hardware wallets. So there's different types of that stuff. I remember back in the days, were like, I think it was called paper wallets when you have your seed phrase on paper.

**Adam [32:20]:**
Yeah, yeah, yeah, I've

done that I've actually put to the face output on a piece of paper and put it in a safe So I had these string of stuff, but here's the problem yet

**Joe [32:28]:**
⁓

you made me feel old. I thought you were talking about cash, like with actual money in it. I mean, I've got that, but okay.

Yev Broshevan (32:33)
you

**Adam [32:33]:**
No, Joe.

So yeah, so hardware has an MTBF, Mean Time Between Failure. That means every piece of hardware will fail. Even humans will fail. There's a certain percentage of time where we know 100 % a human's gonna fail. So even hardware, if you put your stuff on a hardware wallet, what do you do, make two wallets? Because eventually that hardware's gonna fail.

Yev Broshevan (32:55)
Yeah, exactly. That's why you diversify and distribute your assets to different type of ⁓ places where you can store it and diversify vendors and everything. I don't know, like in crypto, can put everything in one pocket, right?

**Adam [33:09]:**
Just give it a yeah, she'll hold it for us.

Yev Broshevan (33:11)
you

Yeah, but honestly, there were... ⁓ there should be probably statistics where people store their crypto. I'm pretty sure that a lot of them on crypto exchanges. Let me like...

**Joe [33:11]:**
Okay, so.

I'm sure they do because people not only can't do it correctly, they don't even know what to do, I'm sure. People can't use a password manager. They're to put their life savings or something.

**Adam [33:32]:**
Well, it's funny you said that, Joe.

And that's the other issue you have, People might have stuff in a certain base wallet. Let's just leave the whole name out. They put their stuff in a base wallet, they have multi-factor authentication, they leave the stuff in there, and they put their password and username in LastPass. I shouldn't say LastPass, but because there was a vulnerability in LastPass. I'm not gonna lie to you, I've used LastPass before.

Everything has everything's gonna be hacked. Everything's gonna be compromised. It's only a matter of one and where ⁓ and my point I'm making is if you put your stuff into a currency a currency application that that trades and holds your value, but you put your password into a password manager Somebody is able to compromise a password manager. They compromise your currency account

**Joe [34:18]:**
Thank

**Adam [34:24]:**
There's no perfect utopian way to store this money. So unless you're doing cash in your safe, that's, you know, like fireproof, because even in your local place, people do that. And then if you're walking down the street in Manhattan and you know, and have a lot of money and then they kidnap you and tie you up in an apartment and torture you, they're going to get that money anyway. That happened, You didn't know about that story?

Yev Broshevan (34:46)
Yeah.

But that is true. This year it's... Yeah, it's crazy. This year I think there more than 30 crypto people was kidnapped, officially reported, because they like they have...

**Joe [34:50]:**
I know people get kidnapped, yeah, I mean...

**Adam [34:53]:**
No, no, it's happened, Joe. Sorry, go ahead.

Yes.

That happened

**Joe [35:04]:**
I'd heard

**Adam [35:05]:**
to a

**Joe [35:05]:**
about that many? Like 30?

**Adam [35:05]:**
f- Yeah, Joel, were you kidding me?

Yev Broshevan (35:07)
It's like officially

reported, you know, but it was a big, story, especially with the guys from Ledger. They're like cold wallets, if you heard about them. So they were like kidnapped and his family was kidnapped in France. So that's, going big. You know, you need to protect not only online, but offline as well.

**Joe [35:10]:**
officially report.

**Adam [35:26]:**
Joe VaaS, it's violence as a service.

**Joe [35:28]:**
Yeah, violence as a service. Well, you know, it's the old rubber hose attack, basically. You know, all these things work. please, you're from Brooklyn. Come on, yes, you have. I don't know.

**Adam [35:34]:**
I've never gotten hit with a rubber hose, so stop that Joe.

Yev Broshevan (35:39)
You

**Joe [35:42]:**
No, but it's true. And it is interesting. guess people, ⁓ and this gets a little, well, does get beyond technology. That's the thing. I guess they don't realize that they've never been rich or something. But all of sudden, if you have tens of millions of dollars, people might, it's not just hackers coming after you. It's people going to come after your family. know kidnapping is a really big deal.

**Adam [36:03]:**
And that's the problem

with cryptocurrency as well Joe, right? It's at the end of the day, it's back to layer eight. Even though we were talking about layer eight compromising somebody from like fishing them, I mean if you have tens of millions of dollars in cryptocurrency, people are gonna know that Joe. They're gonna know that whether it's somebody that works internally for an organization that manages that money, they're gonna tell somebody, they're gonna wait for you outside your apartment.

they're gonna say, me your keys and give me everything, your password and username. It's really scary these days because it's really no different from the guy back in the day, Joe, you and I, you we knew people who were jewelers and they used to bring home jewelry to their house. They put in their wall safe and people would break into their house and tie them up and take their jewelry. Now it's all virtual, but physical access to the people.

**Joe [36:52]:**
Well, we can do the same thing, I guess, right? OK. ⁓

**Adam [36:55]:**
Yes, sir. Yes, like I'm going

to come on this podcast again.

Yev Broshevan (37:01)
Yeah.

**Joe [37:02]:**
I'm going to have to

leap out some of the words you said. The algorithm doesn't like that. So don't be insulted. OK, let's get things a little lighter. OK, so if you look at a lot of code, that's what you do, a lot of these things. I mean, have you had any like, oh my god moments?

I mean, because it's not just like, this application has a vulnerability or something. It's like tens, hundreds of millions of dollars are suddenly really exposed. mean, it sounds like you've come across that stuff, but how, again, how prevalent is that thing?

Yev Broshevan (37:36)
Yeah, definitely.

I mean,

it's getting a bit better. So we look at the code at two different perspectives. First, we do security audits internally. So we have security researchers internally and do kind of consulting business. And also we have a platform, bounty platform called Hack and Pro.

**Adam [38:00]:**
⁓

Yev Broshevan (38:01)
where we have the community of ethical hackers around like probably around 50k by now. So where we we utilize this know crowdsource power and mind to have to find the vulnerabilities. And you know the bug bounties in crypto space is way way higher than in web2. I remember I think it was

**Joe [38:21]:**
I'll

bet because yeah, it's not like you get the exploit or the vulnerability. You got to figure out how to sell it. If you hack it, you got the money, right? Wow.

Yev Broshevan (38:31)
Yeah, exactly. Another problem,

how would you use it then? But it's a totally different story because it's not that easy anymore to use these stolen assets because the exchanges and centralized places will just block them and like blacklist and it would be hard to do something with that. But if we look at the market of bug bounties, usually it's like

5 to 10 percent of the potential loss and one of the stories is like bug bounties for example 6 million when it was 300 million at risk.

**Adam [39:02]:**
Oof.

Yev Broshevan (39:13)
So definitely, bug bounties is a good stuff in crypto in terms of the money you can get. But honestly, the industry practice here is 10 % of the potential loss, and the losses usually are quite high. That's why we have this multiple layers of security with the internal auditing and then kind of external crowdsourced audits when all hackers from all over the world can attack the protocol and legally help them and get their money.

**Adam [39:19]:**
you

Thank

Yev Broshevan (39:43)
as the volunteer.

**Adam [39:44]:**
So yeah, bugger.

**Joe [39:45]:**
Wow. So we've

got to give this a little context of, know, a bug bounty is when an ethical hacker finds a vulnerability and then they give it to a company and the company has, they offer things that depending on how severe it is, they give them, you know, some, some money and you like they do with browsers and a lot of other things. But like with that a hundred thousand or something really critical is a lot. That's a huge one, but $6 million. Oh my.

Yev Broshevan (40:08)
100,000

**Adam [40:12]:**
Thank

Yev Broshevan (40:13)
is not huge. It's kind of normal. But when we come, we can talk to, I think the biggest volunteer is around 10 million for some protocols exchanges. Yes. High.

**Joe [40:22]:**
in crypto you mean? Yeah wow wow that's

**Adam [40:28]:**
So, yeah, I

got a yes no, I got a yes no question for you. You don't have to answer. Have you ever like, you know, cash in on a bug bounty like that?

**Joe [40:30]:**
another world!

Yev Broshevan (40:38)
me personally? No, there's no. I create environment for others to...

**Adam [40:39]:**
Yeah, I'm surprised.

I know, I get it,

I get it, but you know what, think about it this way, you're not doing anything unethical, and you can be living, you know, you can be living probably very well for the rest of your life if you're able to find it because of your expertise, but I have another question for you, Yev, and please don't be insulted. You're a young lady, you look very young, you're a CEO of a company, your Forbes 30 under 30, when you walk into a boardroom or to a CEO,

**Joe [41:06]:**
you

**Adam [41:12]:**
Do they respect you the way you feel like you should be respected? Or like, you know, you'll go back outside and go to the park or something like that. And I know that sounds a little bit demeaning, but people, unfortunately, they don't understand that sometimes youth is better than people our age, because you had that new experience versus Joe and I are still trying to use dial-up modems.

Yev Broshevan (41:36)
Honestly, I had something like that before in my career when I was a student because I started to work in this industry quite early. I think I was ⁓ 19 or something. ⁓ And of course, like coming to clients or clients calls, they were like not expecting anything from me because I'm just, you young student. But ⁓

You know, it's always good to surprise people that you know something and you can help them. But as for like now and the current experiences, I don't have this anymore because... ⁓

**Adam [42:03]:**
God bless you.

**Joe [42:04]:**
Yeah, really.

**Adam [42:12]:**
God bless.

Yev Broshevan (42:14)
You know, when we're even talking about like crypto and digital assets, now these two worlds are trying to emerge because now we can discuss digital assets on the government level, like all these new initiatives from the president.

Of it's getting, you know, it's kind of merging these two completely different worlds from guys from Wall Street and Thewz and Crypto People and Hoodies and Flip Flops. Of course, there's like two different mindsets, ⁓ a total different, and now we need to find the common ground how to make it happen because we see this is already happening and it's super interesting to be a part of this. ⁓

**Adam [42:48]:**
you

Yev Broshevan (42:56)
That's why I would say I'm kind of already old for this because... ⁓

**Adam [43:03]:**
She's like a she's like a gymnast, you know, once you're 18 or 19 years old like a gymnast. Yeah

**Joe [43:07]:**
Yeah, that's it. You're done.

Yev Broshevan (43:09)
You know, because there are lots of people making ⁓ really strong businesses in this area from they are like 20 to 25-ish. Of course, when you're maturing and scaling, there are other people coming, but this genius ideas are usually somewhere in this... Okay, let's say 20 to 30 range. I turned 30 this year, so I'm not in this category anymore.

**Joe [43:35]:**
Now I feel better. Thank God.

**Adam [43:37]:**
So now

she can't claim the 30 on the 30 anymore. Thank God.

**Joe [43:40]:**
Alright, okay. That's

Yev Broshevan (43:40)
I did it before.

**Joe [43:43]:**
right. Well, I gotta tell you, I've spent many years working on Wall Street. And yes, they can be very insular and not take people seriously and not be the nicest people in the world. But the one thing they understand is money. And when someone makes money for them, a lot of money,

They can put up with a lot and there are guys who've done like, you know, high frequency trading and all sorts of stuff and they can go into a boardroom and flip flops and they're tolerated.

**Adam [44:01]:**
Yes, the best friend.

⁓

Yev Broshevan (44:14)
Exactly. That's what's happening. You know, that's what I've seen in the bug bounty industry and crypto industry as well, because a lot of my friends, ethical hackers or like, okay, yeah, ethical hackers. Most of them, ethical hackers, not... No, no, no. mean...

**Adam [44:27]:**
Not over!

**Joe [44:30]:**
Talk about the unethical

ones, come on. Okay. Okay.

Yev Broshevan (44:32)
No, I mean, not traders. So ethical hackers,

got their millions quite early in their twenties. And I think, I think there is like also a problem in that because you're not getting through this like achievements and like natural self-development, self like maturing. And you can kind of already in the stage where you're a millionaire. And I don't think it's good for person.

**Adam [44:39]:**
Ugh.

Yev Broshevan (44:56)
to become a millionaire that early, honestly, in terms of their emotional intelligence, their communication skills and everything, because you are literally spending time with your computer, and when you got this millions, what are you going to do with that? If you don't have friends, you don't have partners, family, and whatever.

**Adam [45:16]:**
Yeah, I agree with you. Yeah, but the problem is, think, and you're probably statistically right, if you become very well off at an early age. But the truth of the matter is, in this industry, we're not known for our ability to socialize. A lot of us are considered people that are like, well, our asset is also our ⁓ negative part of us. We were able to do such amazing things in technology.

But we're not known for being the life of the party. Maybe me, but that's another story. Yeah. But that's the point. Yeah. Go ahead.

Yev Broshevan (45:49)
Yeah, I heard that you were at Emily's cocktail party. You're the one.

**Joe [45:51]:**
Well...

Well, think it depends.

mean, a lot of it really, and this really has to go with not just technology people, like athletes, know, movie stars, entertainers and everything who get very wealthy, very young. think a lot of it has to do with your upbringing and not just in terms of did you grow up rich and you know how to handle money and know people, but, know, kind of having your head on right, you know, and not thinking like,

Oh, I'm the greatest thing in the world, or I don't have to listen to anyone, or even the thing like I don't need to talk to anyone now. That's a sign of, I mean, there's a little bit of a stereotype, but that's also a sign of really not great mental health there. Someone who's quite like that, you know?

Yev Broshevan (46:45)
That's it's great not to

expect much, because of course we're trying to categorize and filter people by age, by appearance, by something, but in this world where everything changing that fast and ⁓ the diversity of expertise and cultures in crypto is crazy big. For example, in my team we have 30 nationalities and...

**Adam [47:10]:**
Wow.

Yev Broshevan (47:11)
It's really interesting to have this diversity in terms of mindset when it comes to security, because that's what you want to have. You want to have different opinions and different type of vulnerabilities, a way of thinking, because this business is that decentralized and global that you need to protect from every possible site.

**Adam [47:30]:**
It's

interesting to say that because that's a Google mindset. Google's mindset is that diversity and diversification both on every level, whether it's nationality, gender, sexual orientation, brings the diversity for creativity and being able to do things. But I think you have over 100 people working for you now, right? Is that correct? Yeah, so I got to tell you again, I'm really impressed by

Yev Broshevan (47:50)
Yes, yes.

**Joe [47:52]:**
hundred people.

Yev Broshevan (47:54)
I'm just 15.

**Joe [47:55]:**
Yeah.

**Adam [47:58]:**
you know you at an early age you know and there's also some jealousy and envy and I'm envy I wish I've done something like that but at the same time I applaud you it's it's it's not an easy ⁓ not an easy accomplishment especially and I and I know people are to probably yell at me I'm gonna get a hate mail for this but when when you're when you're a woman you're not really seeing the same as you are as a man but what I've seen lately is so much more women out there

that are doing the same type of accomplishments you are in the technology. ⁓ We've had a lot of women on there like, my God, one woman funded her own organization and she's doing very well with incident response. Another woman became the CEO of another company. So it's really impressive because back in the day, if there was one woman in the room, you were surprised. Now it's like, forget it.

Yev Broshevan (48:52)
Yeah, that's true.

**Joe [48:52]:**
Well,

it depends. mean, it's still insecurity. It is still really heavily skewed towards men. It is getting better, a lot better.

Yev Broshevan (48:57)
Yes, but it's getting better. It's getting a way better. You

know, and especially so I always been in this kind of circles because first I was in like traditional security, cybersecurity, and we always were like really few of us. Then when I switch.

**Joe [49:13]:**
You in traditional cybersecurity, what, for a week? I mean you started

**Adam [49:17]:**
Hehehehehe

**Joe [49:17]:**
with crypto like so long

ago. ⁓

Yev Broshevan (49:19)
for couple of years.

But then when I switched to Web3 security, it's like even smaller circle. But now we have more female led businesses in Web3 security. Probably I can count this onto my hands, but it's a way more progress than we had before.

**Adam [49:41]:**
That's the question I have for you, Dave. What got you from traditional cybersecurity? What prompted you? What woke up in your mind that said, I want to get into cryptocurrency?

Yev Broshevan (49:52)
You know, I've always loved innovation and possibility to change an influence to something and when I learned about crypto in 2014 from my professor in university and then I learned about Bitcoin from another guy who gave lectures in university I said like, okay, this is something cool. You know, it's

you know, it's kind of not widely accepted. There's specific technology that might have potential and might not. A lot of people saying it was scam, was a pyramid, whatever. But I was fascinated by the technology itself. And then naturally it was curious, like how to break this technology. Because I think the hacker is also about the mindset you have. It's either you do it in like everyday life or in your like computer programs, right? It's how you think. And for me, I was going

through like, ⁓ let's get a normal cybersecurity like hacker, then to Web3 hacker. Now I run the business, so I do kind of gross hacking and trying to find the ways, creative ways to solve the challenges that I have. And also recently I got interested into biohacking, which is kind of ways how to hack your body. So I think it's also about the mindset.

**Adam [50:54]:**
you

Thank

**Joe [51:08]:**
Okay, I was

going to say curiosity. That's great. Everyone be curious. And you know what one of the best ways to satisfy your curiosity is? Listen to podcasts and subscribe to them and like them and follow them. You know, like for example, I heard the security cocktail hour is pretty good. And if you have questions, put them in the comments. It will satisfy your curiosity.

Yev Broshevan (51:11)
Yes.

next life.

**Adam [51:19]:**
Like which

one Joe? Which one? Which one should I listen to?

Yeah.

Yev Broshevan (51:26)
By the

Where's cocktails in this podcast? didn't get it.

**Joe [51:35]:**
Well, actually, ⁓ I did pour a glass of wine, and we didn't usually get to it. ⁓ I think the drink was going to be, you have said, non-alcoholic wine. And I promise this is non-alcoholic. Absolutely. Maybe. Don't hold me to it.

**Adam [51:35]:**
I could s-

Yev Broshevan (51:49)
Really?

**Adam [51:51]:**
Well, so

Joe came up with the idea that after hearing some of the things that are going on, you're gonna wanna have a drink. So the whole premise of the Security Cocktail Hour, for those who don't know, is basically a couple people sitting behind a bar talking about security. So this is the virtual bar, this is the virtual drink, well it's real drink, and this is us virtually talking at a bar. And you're more than welcome to go to a bar with us, you can get orange juice and we can hang out, but this is what we do.

Now you got me curious, Yev. What have you done in biohacking?

Yev Broshevan (52:26)
Yeah, okay, first let me pour my non-alcoholic wine. It's zero, zero percent. ⁓

**Adam [52:30]:**
Very nice.

**Joe [52:31]:**
Alright, there we go.

zero percent.

That's a selling point. I mean, I'd pick that up and say, like, what the hell is this?

Yev Broshevan (52:38)
I think it's

a 0.5 usually in this kind of drinks because you can't like de-alkalize it like fully.

**Joe [52:46]:**
I

exactly going to say that, you know what? I'll tell you something. And I learned this recently. Cheers.

**Adam [52:54]:**
Cheers.

**Joe [52:57]:**
I learned recently that ⁓ I think they can say that like in Europe or something. They can put 0.0. But in the US, they're not allowed to say it actually has nothing because it has a little bit. maybe it was the reverse. I don't know. Anyway, so.

**Adam [53:11]:**
some sugars are alkalized no matter what.

Well, she's not in the US right now. I'm not gonna say where she is,

**Joe [53:20]:**
doesn't matter,

in an undisclosed location outside the US. All right.

Yev Broshevan (53:25)
Interesting that in New York I stopped by some wine shop and asked for non-alcoholic wine and they said like no we say like sell only alcohol here so non-alcoholic is only in supermarkets

**Joe [53:38]:**
Yeah, of course. You see, that's a look. Look at America. You go into the liquor store and ask for something non-alcoholic. They'll look at you like you have three heads. did you not see the sign? You know?

Yev Broshevan (53:40)
Yeah, no,

**Adam [53:49]:**
Well, there's times

I've gone to a bar and I'm like, can I get a seltzer? They're like, yeah, what do you want with it? I'm like, no, just a seltzer. Because I'm not big drinker. But, um...

Yev Broshevan (53:57)
you

**Joe [54:00]:**
Well, actually,

we're fooling around a bit, but we should say, in places that sell beer, you're typically the non-alcoholic beers and stuff. And if you go to a bar, if it's a good bar, you can't get something non-alcoholic. We're not all drunks and force people to drink in the US. Not everyone in Texas has a gun either. ⁓

**Adam [54:16]:**
Yeah, I bet. No, we're not. Absolutely respect everybody's choice.

Yev Broshevan (54:22)
Thank

**Adam [54:24]:**
But I still, I gotta get to Yev, I gotta know what viral hacking is. I was, God, I don't even wanna say Yev, so don't make fun of me, please, and don't call me old. Back in 1989, I was going to a community college, and that's when viruses came out, and I did a presentation on viruses, and somebody says, can you get, can a human get a computer virus? And back then, I left.

But nowadays you don't even know anymore about proteins and biohacking and whether or not your synapses is going to be able to transfer to electronic pulses to a human. You never know anymore. this is, wait, wait, wait, wait, wait, wait, wait, wait, No, no, no, but, but, but I'm going off on a rant. So I had, so I wrote an assignment the other day about emotional intelligence and AI and wellness and everything else. And I say,

**Joe [54:58]:**
Well, when she says biohacking, don't think it means like genetically engineering viruses and stuff. mean, ⁓ god.

**Adam [55:16]:**
back in when the Wright Brothers went to go fly a plane, everybody looked at them like, what are you talking about? No one's ever gonna fly. And I bet you, maybe not in my lifetime, there'll be a consciousness with AI. But until that day, we find out what that means. And that's the whole conversation I had with my friend, Peter, He goes, this is something you'll never experience in this universe. Either someone has to bring what consciousness is, that's another story, but.

viral hacking, you still got me curious.

Yev Broshevan (55:48)
Okay, so ⁓ where to start? I was referring to mindset and honestly at some point of life I said like...

Literally, my body is a black box for me and I don't know like how it works, you know, what metrics it has and how I can, you know, how can I do ⁓ even with this anything. So first, first what I, you know, at least adding a bit of consciousness to your physical body, because I know that we're like just using it and then when it hurts, we do something. And honestly, I find it fascinating the, the

**Joe [56:10]:**
you

Yev Broshevan (56:32)
Connection between security and health if we look at this So we need to make a preventative measures for security right not to make a bridge happen same we should do for health we need to prevent like any possible like diseases happening to us and the same as Security health is also conscious process. You can't do it once and it's just you know done for forever, right? So at one point of time I started thinking like how my body even works like what is

my source code? How can I fix it? How can I influence it? And there is a guy, his name is Dave Asprey. He claimed himself to be a father of biohacking. He actually used to be a security engineer and he started doing his biohacking journey like 10 years ago or more.

**Adam [57:05]:**
Wow.

Yev Broshevan (57:23)
And it's like, okay, here's a clear, clear kind of like ⁓ connection. So you analyze your body and influence the metrics you want to influence and trying to find the shortcuts, back doors, how to make your body recover better, stay younger, be more active and stuff like this.

**Adam [57:42]:**
When

you read your book, Joe, we had somebody that spoke not exactly about that, about the throughput in your brain and how things are manipulated and how kids are being influenced by social media.

**Joe [57:58]:**
Well, yes,

that was when that was interesting. you know, I'll tell you this as someone with a few more miles on this body than you have. ⁓ That's great. And starting to take care of your health and worrying about it when you're young is very good. And we've talked about it before too, especially mental health. There's been a lot of issues in mental health and security. I like to think it's getting better, but it's still there. you know what? ⁓

**Adam [58:00]:**
Yeah, that was it. Yeah.

**Joe [58:27]:**
before you go hack too much and listen to the executed guy. I don't know what he says and everything, but remember we do have doctors who know a lot about how your body works who can help you with that too.

**Adam [58:40]:**
But I think you have more of reflection on the mental ⁓ part of it and how that transfers to like, you know, what can you do in your mind in order to maybe need to meditate in order to make sure before you do something that you don't put yourself and you lower the vulnerability to certain things. That's I think what she's talking about. And it's funny, have Shameless Plug, Government Tech Con (GovTechCon), I'm going be on a panel about mental health and security people. So that's coming up in September. I don't know if this podcast will come out before that, but

People can rewatch it, but I'm going to be on panel.

**Joe [59:11]:**
I

thought you were talking about drone hacking. No? It's mental health?

**Adam [59:15]:**
No, no, that's government

tech, Conor. I'm on six panels. One of them is...

**Joe [59:19]:**
you're on six,

⁓ you see, I'm losing track. You're so busy.

**Adam [59:22]:**
Joe,

I am so important in my own mind, it's insane. If I had the amount of money about how important I was in real life, I'd be broke. Wait, I am broke. Okay, it's all good.

**Joe [59:26]:**
Seriously.

Yeah, really. Okay.

Yev Broshevan (59:34)
What?

Honestly, so what I found the most fascinating throughout this journey is getting kind of my source code. So I did a DNA test where they showed me different enzymes and pathways, how it all come together and how different elements absorb in my body or doesn't absorb. And it was like, ⁓ wow. Because, know, like everyone takes just like vitamin C, vitamin B, whatever, just take vitamins or supplements to, you know, feel better. But we don't take it

on the features of our body. And when I got this test, it was like a big diagram with all these pathways and different colors. It was like a kind of algorithm, right? What works and what doesn't.

this like blood tests and different DNA tests helps you to understand your body and understand the algorithm, how your body works. And in this way, when you know the algorithm, you can find ⁓ shortcuts to what you need to fix. ⁓

Joe Patti (1:00:35)
Okay, well, you know what? My algorithmic expert, my doctor, keeps telling me to, you know, drink less, but that... It hasn't seemed to take for some reason. I don't know.

Adam (1:00:47)
Well,

for me, Joe, like I go every three months for blood tests and they constantly analyze my blood. Constantly. Like, what do you have for this? What do you have for that? So unfortunately, I'm not biohacking my body. I'm listening to them about taking potassium citrate to stop this and taking this to stop that. It's just the way it is. But every three months I go for a blood test. So it is what it is, Joe. I guess you're biohacking in a way.

Joe Patti (1:00:55)
Yeah.

Okay, that's right.

Adam (1:01:16)
because these doctors want to make sure you supplement one thing or decrease something else.

Yev Broshevan (1:01:20)
But you ⁓

Joe Patti (1:01:20)
Well, I go to the doctor,

I got to go this week for my physical whatever. Always tells me the same thing. Always the same thing, you know, lose weight, don't drink so much, whatever. That'd be 400 bucks. I'm like, thank you. That's real helpful. So anyway.

Yev Broshevan (1:01:35)
It's good recommendation,

but how to implement this, this is totally another topic. But what you talked about, Adam, regarding the gene editing and body replacement and freezing bodies to find the cure for the disease that we have now in the future, it's also a big topic ⁓ in longevity and people and scientists working on that. is first labs and companies that do gene editing, but on the legal level in many countries,

is prohibited to go to other countries. So it's still experimental, probably in 10 years or something we'll have more of that possible, but still it's not a much solved question.

Adam (1:02:06)
Yes.

So,

Joe Patti (1:02:18)
But

Adam (1:02:18)
my family, to it.

Joe Patti (1:02:20)
I'll tell you, I want to get frozen. Because you know, and maybe they were... Look, you got nothing to lose. You're already dead. Right? You got nothing to lose, even if you got a slim chance. So what? Come on.

Yev Broshevan (1:02:23)
Really?

Adam (1:02:28)
Yeah, I don't want to live longer than... no, no, Joe. I don't want to

wake up a hundred years to meet my great-great-great-great-great-grandchildren.

Yev Broshevan (1:02:39)
No, it's interesting. I met one guy, he

runs the company that like freezes bodies and he frees not only people, but also pets to be when you wake up, you still have someone, you know, like close to you. So they freeze both people and pets.

Joe Patti (1:02:43)
Yeah, cool.

Adam (1:02:48)
Yeah.

Joe Patti (1:02:54)
That's...

Well, that's a bit much. Personally, I'm waiting for my cats to die. They drive me crazy. They're not getting frozen.

Adam (1:03:01)
you

I don't, when it's time for me to go, it's time for me to go from this world. But from a standpoint, I'll still go to my doctors and I'll still have them analyze my blood and see what medications and drugs, because like everybody else, everybody has these risk factors, whether you're Jewish or you're black, sickle cell anemia versus the different things, we all have.

traits based on our religion and our I know religion sounds weird because because of the religion where you're from we all have these traits in our blood that bring up diseases so sometimes it's good to analyze it but I gotta tell you yeah I'm scared to ever do any of genealogy things because I don't want that stuff to get out there with those those ⁓ with those DNA markers

Joe Patti (1:03:50)
Well, I think we're going to end on this note of, I don't know how we got from crypto to all this, but take care of yourself. Do what works for you. It is important to do that. Your health is important.

Adam (1:03:57)
hacking

Yev Broshevan (1:04:06)
Yeah, it's

important to invest both in your health and your security to be a resilient person and build resilient systems.

Joe Patti (1:04:15)
That's right. So don't protect your keys by putting them on a thumb drive and swallowing them. That's a very bad thing to do. OK. Well, yeah. Thanks so much for joining. This was great because we really joke about not being up to date. But we really did learn a lot. This is interesting. what you're doing is a new and really important high stakes application of security.

Adam (1:04:16)
Yeah, I want to back up.

Joe Patti (1:04:43)
Yeah, there's real money at stake here.

Yev Broshevan (1:04:45)
Thank you for having me.

Thank you, Joe. Thank you, Adam. You really have a great sense of humor. I like it.

Adam (1:04:52)
Thank you.

Joe Patti (1:04:53)
Thanks. Alright, thanks everyone for listening and watching. We'll see you next time.

