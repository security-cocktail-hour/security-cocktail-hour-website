---
title: "Flipper Zero and Other Totally Legit Hacking Tools"
date: 2023-04-20
draft: false
guest: ""
category: "Educational"
duration: "38:04"
image: "/images/episodes/episode-001-013.png"
description: "Joe and Adam decode the Flipper Zero hype: what it does, how it fits in security, and the ethics of hacker tools."
platforms:
  youtube: "https://youtu.be/BVca3X8wE_c"
  spotify: "https://open.spotify.com/episode/0olsN2LKLn09wOLpnxqeIH?si=ea00fe99013b48ca"
  apple: "https://podcasts.apple.com/us/podcast/security-cocktail-hour/id1679376200?i=1000609957037"
  amazon: "https://music.amazon.com/podcasts/d11e431a-f7b1-4bb0-8671-024afce9ade6/security-cocktail-hour"
guest_bio: ""
---

Joe and Adam decode the hype around the Flipper Zero, the latest testing device (i.e. hacker tool) to generate buzz in the security community. We go through what it does, how it fits into the wider security world and the proper use and ethics of these tools.

## Episode Highlights

- White hat vs. black hat: The ethics of security tools
- Responsible disclosure: When and how to report vulnerabilities
- Why Amazon banned it (and why that misses the point)
- Real stakes: Cars, building systems, and IoT vulnerabilities
- Debunking the hype: What the Flipper Zero CAN'T do

### Listen Now

Tune in to hear our discussion on this topic.

## Full Episode Transcript

*Joe Patti (00:00)*
It's five o'clock somewhere, time for the Security Cocktail Hour. I'm Joe Patti. For over 20 years I've been working in information security and knocking back martinis all over New York.

*Adam Roth (00:15)*
I am Adam Roth from Staten Island. Locksmith, EMT, love to box. In our rare occasions I've been known to engage in cyber security. Let's go!

*Joe Patti (00:26)*
Alright, so if you've been listening you might have noticed that Adam is a bit more of a technical guy than I am. I've been a manager for a bit, but Adam is a serious network engineer. So you want to tell everyone a little bit about your vast background and experience in this area?

*Adam Roth (00:46)*
Well, I want to say network security, cyber security, physical security engineer.

*Adam Roth (00:54)*
Yeah, let's get physical.

*Joe Patti (00:56)*
Adam also loves the integration of physical and network and cyber security, which not everyone, including me, completely appreciates, to be honest.

*Adam Roth (01:06)*
Yeah, so I have a background. I started off as a network security engineer, but at the same time worked on physical security projects to integrate into both network and cyber. I enjoy having the hands on and just getting my hands dirty and jumping right in. Over 20 years. You Joe? Yeah, very funny.

*Joe Patti (01:30)*
60. I've been on a spaceship travelling towards the speed of light. Now, I have been in this wonderful business in the neighbourhood of 30 years. I've been doing security for most of it for quite a while. I started out in the technical world, but now I'm really, really more of a manager, a strategist, not just a cyber person, but a risk professional, I suppose. That's the latest buzzword you got to morph yourself into because we're always evolving.

*Adam Roth (02:02)*
Yeah, it's very risky.

*Adam Roth (02:04)*
You have to work in compliance, risk, into any conversation.

*Adam Roth (02:11)*
Just the other day, I went into the supermarket and I was risk overt.

*Joe Patti (02:15)*
Really? Why is that? Were the bananas looking a little brown? What was it?

*Adam Roth (02:21)*
I was just using the word risk.

*Joe Patti (02:23)*
Well, that's good. Well, fortunately, you go into a good supermarket, but there are always risks.

*Joe Patti (02:29)*
We'll be talking about those and how, what risk management means at some point. I have some very, very interesting opinions on that. For today, this is more The Adam Show because we're doing a bit more of a technical session here, or at least we're going to start talking about technology.

*Joe Patti (02:47)*
Adam loves,

*Joe Patti (02:49)*
among other things,

*Joe Patti (02:52)*
hacker tools or more properly known as security testing devices, security devices. You have quite a collection, don't you?

*Adam Roth (03:03)*
Well, I've had a collection. I've sold them. I've bought more. There's two things I love. I love hacking tools and ice cream. And ice cream, that's true. So, yeah, I love hacking tools.

*Adam Roth (03:16)*
Hacking tools kind of challenge you as well as helps you to determine the risks in your organization which allows you to determine what you need to be compliant for. So, I worked this towards in there. In this particular case, I think we're talking about the hacker zero.

*Joe Patti (03:32)*
Well, let's talk. First, let's talk about what we mean by hacking tools. So, everyone knows.

*Joe Patti (03:39)*
Basically, it's like the stuff you might have seen on Mr. Robot. I think that's probably how most people are familiar with it. And you actually have had some of those things, haven't you?

*Adam Roth (03:47)*
Yes, I have had some of the tools from Hack Five. And they have a lot of nice tools. I mean, I don't think I have a room big enough to hold all those tools if I was to buy it. Nor do I think my wife would let me spend that much money. But I'm open to receiving them if they may be.

*Joe Patti (04:07)*
Rule number one of hacker tools, never take any that people send you for free because they're guaranteed to make you unhappy eventually. Put it that way.

*Adam Roth (04:18)*
Depends. But yeah, I mean,

*Adam Roth (04:21)*
let's be honest. There are tools that come from reliable places that have been compromised before they even hit the floor. But in this particular case, when we speak of hacker tools,

*Adam Roth (04:35)*
they're kind of like pen testing. And what a pen test is, is you're looking for a pen

*Joe Patti (04:40)*
test is a penetration test. It's when you try to break into your own stuff. It's a wide term for that. Yeah. Please continue.

*Adam Roth (04:48)*
Well, you might not be breaking your own stuff. You might be breaking into other people's stuff with their permission.

*Adam Roth (04:54)*
Yeah. I want to make sure we say that. But by the way, you should never pen test or penetration test anybody's network without permission in writing. But that being said, what hacker tools do is it exploits vulnerabilities or it looks or discovers vulnerabilities. So I'll give you a quick example of some vulnerabilities. Maybe you're going to use a hack tool to run commands at a high rate of speed that normally a person couldn't have done by using a tool. Or you might use a hack tool to exploit a vulnerability, maybe in radio, like a flipper zero and be able to copy a signal and replay it to open up maybe a Tesla charging port.

*Adam Roth (05:42)*
There's a lot of different things that you can test. And the reason why these tools can be used for good is when you're testing, you know what you have to plug up or or fix so people can't exploit that themselves.

*Joe Patti (05:55)*
That sounds like sound. I mean, you know, penetration testing has been around for a long time. And what most people know about it, I think is like testing web applications like, you know, your bank or any other company you're doing business with. They have a website and they they don't just do it themselves. They also typically hire people, security consultants to go in and test it to see if there are bugs and bugs that can be exploited to break in. And things are regularly found. Writing those are very difficult. Sometimes they're pathetically easy to find, which is terrible. But there are also tools that can be used to do it in an automated way, software tools. But then just about anything, really, you can test like and as more things become, you know, enabled with more electronics and more, you know, more computers and CPUs, more and more types of testing are going on and are and are actually necessary. I mean, you'll you'll see on on TikTok and on YouTube, you know, like I say, oh, I broke into a car. I did this. And there are, you know, some of them are making trouble and they are doing some things that maybe they if they're doing more than demonstration, they shouldn't be doing. However, the people who produce those, it's actually very important that they have access to those things to to find the vulnerabilities before the bad guys do because the bad guys will any vulnerability, any problem or design defect, whatever it is. The bad guys will find it. It is best that you find it first.

*Adam Roth (07:25)*
Yeah. So I don't know if this is really a true story. I don't think anybody can validate it. But I think pen testing goes back to the Trojan horse with the creeks and the in the during the Troy was the Trojan War. You know, when they all the children were the into Troy. I'm sorry. During the Trojan War into Troy and all those soldiers hid in that. Big wooden horse and then they pushed a horse into the territory and then they came out and they started, you know, they're fighting. That's well, well,

*Joe Patti (08:00)*
that wasn't a great penetration test. That was an actual penetration. Those are the bad guys. Those are bad guys. Breaking it. If the Trojans had tried that themselves without telling their own soldiers, that would have been a pentest. I suppose. That's true.

*Adam Roth (08:15)*
I'm sorry. I apologize.

*Joe Patti (08:17)*
No, but that it illustrates the point, whether you realize it or not, Adam, you're a genius.

*Joe Patti (08:24)*
You know, you should be trying these things first. And one of the things that, you know, from a home standpoint that you can do with some of these tools or see, it's like, you know, you may not realize how easy it is or or how difficult it is. You may want to know where someone to drive by and unlock your car or start it or open your garage door or those fancy new electronic locks they have. You know, we understand if you're interested in it, people understand lock picking pretty well. But, you know, how those new connected home systems work and how easily they can be opened. Don't know they need to be tested and need to understand what those are if we're going to count on it.

*Adam Roth (09:04)*
So before we jump back into the Flip of Zero, I appreciate you validating or correcting me on the story. I know you were there. That's how you were able to.

*Joe Patti (09:13)*
I was not there for the Trojan War. I was only there for the Roman Wars. Remember my real expertise is. Oh, sorry.

*Adam Roth (09:19)*
OK. But but but that's exactly what the Flip of Zero does. Right. It takes some of those. Well, it does more than radio, though. People concentrate on radio with the Flip of Zero. It allows you to capture maybe someone opening up a car door and then you can replay the car door. So you have that in your pocket or you have that in a car and you're standing across the street and you listen to it and then you replay it. That's what some of the.

*Joe Patti (09:46)*
Basically, I think it will pass within it. It's a little computer and it has a number of radios at different frequencies and use for different things. And yes. And I guess you can go through those. But, you know, each of them can obviously listen, but it can also record and play back. And that can be a way of trying to break into systems now. And you can find out the newer, better ones. I think we've talked about this before. The newer, better ones should not be so easily susceptible to a replay attack because that's what that's called.

*Adam Roth (10:15)*
But they shouldn't be. Yes. I mean, so it's a little bit different with cars, right? Cars, people don't understand that you really need.

*Adam Roth (10:25)*
To update the firmware in your car and you can do that from your entertainment center. So a lot of the companies are allowing you to update the firmware to these attacks.

*Joe Patti (10:36)*
It depends. But some cars are over the air. Some you still have to take into the dealer and they have to do it themselves.

*Adam Roth (10:42)*
Yeah, it's true.

*Adam Roth (10:44)*
That's what that's what the Flip Zero allows you to do, right? Some of the less sophisticated remote controls and and radio, radio built into some of these cars allow you to capture the signal and replay it. Same thing with your your IoT devices at home, your remote controls for your TV's, though it's less sophisticated.

*Adam Roth (11:08)*
There are a lot of things you can replay. And not only does a Flip Zero do radio, but when they use a USB and you plug it into a computer, it allows you to do replay attacks as if you want a keyboard or find vulnerabilities by scanning. And some of the firmware that's out there that are alternative firmwares, other people have created have become extremely sophisticated and allow you to do some real crazy things. And it's gotten so bad

*Adam Roth (11:38)*
where people are so frightened that Amazon just recently said, we're not we're not selling Flip Zero anymore because it can be used as a card skimming device. I mean, maybe they shouldn't sell knives because, you know, not only can you cut fruit, but you might be able to rob somebody.

*Joe Patti (11:53)*
And, you know, the thing to remember, too, about the Flip Zero and about well, about this one in particular, is that it combines a lot of different things. And in a second, we're going to run through all the different radios and the different things it can it can do. But, you know, one of the things that's nice about it is that it takes a lot of different a lot of different capabilities and puts them in one convenient package. It's that's nice to work with, you know, all these things before. It's like, yes, if you can use it as a card skimmer, believe me, the bad guys, they have no shortage of card skimmers that they can get a hold of. All these things that we're talking about were not as far as I know. Maybe they do have a few unique things. But as far as I know, the at least the vast majority of what the Flip Zero does have been available in other devices, either commercially available or homemade by the bad guys for quite some time. And that's what makes it useful that it brings to a wider audience, the ability to, you know, see what your exposures are and understand these things.

*Adam Roth (12:58)*
So, you know, I think you and I have spoken off air about, you know, the Flip Zero is also considered a Tamagotchi. And when you say Tamagotchi, you think about those devices.

*Joe Patti (13:09)*
I originally thought it was a little toy which terrified me. But yes, you corrected me.

*Adam Roth (13:15)*
Yeah. Well, it's kind of a Furby, but it's electronic Furby. It's a screen. For those who don't. Yeah, for those who don't know, the Tamagotchi was a virtual creature that you had a feed. And when you put multiple Tamagotchis together, it created an ecosystem.

*Adam Roth (13:31)*
Well, the same thing with the Flip Zero. It's a it has a dolphin built in there. And when you put other Flip Azeros near each other, you can play. So it kind of, you know, gives you that toy effect. But at the same time, it's a very sophisticated tool that will allow you to do NFC and RFID, NFC is near frequency contact. So if you have a credit card in your hand, there's a chance you can read the credit card or your access card to your building, some more sophisticated credit cards. I mean, access cards and credit cards. It's very it's harder to read, but you have that capability.

*Joe Patti (14:05)*
OK, so let's run down. I'm going to give you a quiz on this. I actually like this.

*Adam Roth (14:10)*
Oh, no, no, no, no, no, no, no, I don't want to.

*Joe Patti (14:12)*
No, let's run down what it actually has. And remember, this is we're talking about functions that the Flip Zero has. But these are things that other devices, too, that people are using are basically hacking otherwise with, you know, with other techniques and other devices that they're playing around with to find the vulnerabilities. So you talk about NFC near frequency communication, right?

*Joe Patti (14:37)*
So what what uses that?

*Joe Patti (14:39)*
What can you play around with that?

*Adam Roth (14:41)*
NFC actually, well, you can use if you go to a gas station, you go to an ATM, you take out your credit card that has the built in smart chip and then you wave it in front of that contact. That's the credit card gas pump. And yeah, that's NFC. And the phones, too, like Apple Pay, Google.

*Joe Patti (14:59)*
Yes, they call it.

*Adam Roth (15:01)*
Right. And when you board a bus in New York City or even the trains, you use an NFC also to enter into. Oh, yes.

*Joe Patti (15:09)*
And in New York now, having a, you know, forget about tokens, but having a metro card is like very uncool, totally old school. OK,

*Joe Patti (15:21)*
so it does that. Then there is RFID, which is probably much more pervasive. That's an older technology that's been around forever, right?

*Adam Roth (15:29)*
It's older, but it's widely used in RFID is useful. Yeah, they use it many everywhere from law firms to find in files that they misplaced to putting it on shirts and pants in stores to track inventory.

*Adam Roth (15:45)*
And and some people claim it's built into money. I don't know.

*Joe Patti (15:48)*
I used to tell my wife that, but I think that's a that's an urban legend. That like what? Yeah. Years ago, when they put that little metal strip, the idea was they could tell how much money was in your wallet. I don't think that's true.

*Adam Roth (16:01)*
Well, I don't think it was. I don't think it was meant for that. But no, it's anti-dependence. That's a old rumor. But yeah. But our RFID is basically radio frequency for tracking objects. And it can even in RFID is even part of your access cards and security. I mean, the goal is that you're able to track something with readers all over a location or just a single location. So if you're in a building and you're walking around maybe a government building, they'll know what floor you are or what area you are.

*Adam Roth (16:38)*
But RFID is more passive than active, I think, because you have to be energized by the reader. But I'm sure they have active RFID as well.

*Joe Patti (16:48)*
OK, then there is Infra-ed, which is another pretty pervasive technology, TV remotes and whatnot.

*Adam Roth (16:57)*
Yeah. Yeah. Infra-red is useful. A lot of different things. You know, people when they think about infrared, they usually think of remote controls, but infrared was used on actually, you know, computer stuff where you can actually send code to from.

*Joe Patti (17:15)*
I remember that. If what I haven't seen that in years, that's right. You can put like two computers next to each other and you had to put them together just right. So the whole thing went and it was really slow. And if you like, you turn the light on in the room to bright, it wouldn't work. I forgot about that.

*Adam Roth (17:33)*
Though I was very serious, the Israelis had a UAV or drone and they put kind of like a electronically controlled laser pointer and they injected malware into a laser printer's infrared to see if they can do it. That was years ago.

*Joe Patti (17:47)*
But they were drawn outside your window. You know, we record these. We have video on for us. No, you sure?

*Adam Roth (17:52)*
No, I have. I have my my life for zero tracks for the future.

*Joe Patti (17:57)*
Few more things it has sub one gigahertz, which just sounds so cool.

*Adam Roth (18:03)*
So sub is below one gig and usually that's like 433 megahertz or 300 something megahertz. That's for garage door openers and other types of formerly licensed band

*Adam Roth (18:19)*
bandwidth for certain frequencies. You know, like if you open your garage door, I think it's 433 megahertz. But it's also some of your remote control lights and other things that send signals over and a remoteless key systems like you have listed in the past.

*Adam Roth (18:39)*
They're not very terribly complicated devices, so there's no real either encryption or changing frequencies. So it's very easy to copy. So if you're standing outside your neighbor and they're opening the garage door, you can replay it. But they also have a brute force built into the flip zero. That will go through all the signals and all the normal remotes and try to write.

*Joe Patti (19:02)*
And that could be good for thieves. You want to be careful with that. You know, that actually is, you know, with some of these things,

*Joe Patti (19:11)*
I know I've joked about it in the past where you say you can torture your neighbors by changing their TV channel or making their room too hot or something like that. But, you know, in your home, you know, now that we have garage door openers now, guys can do drive bys, try to open them. Now, the same thing is starting to apply to, you know, your doors if you have electronic locks on them and other things in your surveillance. So we really need and we talked a bit about that in the in the home security podcast. We really need to start paying attention to that. And, you know, these devices, like I say, they give you they give you a very good idea of what the bad guys can do. And, you know, hopefully long term, as people do more testing with these, and publish it, that's a good thing because that that will make the manufacturers improve the security of these devices.

*Adam Roth (20:01)*
And that's exactly it, right? If we look at it from purely a cybersecurity standpoint and we look at zero days and someone publishes that, they found a zero day that kind of motivates the vendor or manufacturer to to to close that loophole or close that vulnerability so that it doesn't happen in the future. If people use these tools, as long as they're not using it to actually gain something from it and they're more considered white hat hackers and black hat hackers,

*Adam Roth (20:33)*
for those who don't know, white hat or is are the honest ones in the black hat hackers are the ones that are do things for malicious reasons or to gain money.

*Adam Roth (20:44)*
As long as they're doing it from a white hat standpoint to show these vulnerabilities, it actually solidifies some of these gaps and helps you to prevent other people from doing it. So these tools could be used.

*Joe Patti (21:01)*
There's also something called responsible disclosure. That's something from software security testing that kind of applies to a lot of other things where if you're a white hat hacker, whether you are employed or just or just self profess doing it on your own, you know, it is not considered good to just publish to the world a big vulnerability. It's there. There are actually accepted protocols for telling the manufacturer saying, hey, I found something. Please, you know, fix this before I choose to tell anyone. And that's something we can do to a whole other whole other podcast on, especially when we talk about vulnerabilities.

*Joe Patti (21:42)*
But so those

*Adam Roth (21:43)*
others, I want to. Yeah, I'm going to add one more part to that. And we probably should go into a separate conversation about responsible disclosure, but, you know,

*Adam Roth (21:54)*
you know, when you're using these tools.

*Adam Roth (21:56)*
And you're using a flip of zero and you find a vulnerability, which you could, you know, you're testing, you're looking at radio frequency or and you find something. The question is, do you go out and publish it on Twitter or Instagram or Facebook right away? Or do you give that manufacturer or that vendor the 90 days or 60 days or 30 days that they can to patch it up and then publish it? So, you know, you got to think about I know we're going to touch on this a little bit later, but you got to think about the ethics involved of what you're doing. So it's not just about being playful and open up your neighbor's garage door. It's about the responsibility you have as an individual and how you don't put other people in jeopardy or in a bad position.

*Joe Patti (22:44)*
That's right. And that gets into some other things. As we will probably talk about this when we do more on the Internet of Things. But, you know, now that we're starting to control more things in the physical world like cars and like like cars and like building management systems in particular, the security of them becomes very important as you're testing that you don't mess it up, mess them up, obviously. But, you know, also that you're buying things that are secure. You know, it was very interesting in the past few years where, you know, areas that, you know, buying a little device for something wasn't that big of a deal. A lot of HVA systems for, you know, buildings, they would just say, oh, well, whatever, it's internal. You know, you need to go into the building to use it now that they're connected to the Internet. You know, you really don't want the elevator systems or the power to be going out in the tall building because someone acted. That's raising the stakes. Yeah.

*Adam Roth (23:43)*
And when we look at things like that with the Flip is Zero, Flip is Zero has had this profound effect of not only that tool funding vulnerabilities, but people going out there and figuring out what are the vulnerabilities are there with cars. So as you probably have seen, and I'm sure you have, people talk about the CAN bus and cars and how they can replace the light on a car or move the molding over a little bit and connect to a car system by disconnecting to the headlight of a car.

*Adam Roth (24:12)*
So people are finding, oh, okay, Flip is Zero can do this and this to a car. What else can I do to a car? And as people find more vulnerabilities, they're going out and discovering it. I think to a point where some insurance companies now are not ensuring certain cause because the vulnerability can't be protected against.

*Adam Roth (24:31)*
But, yeah, we need to be careful. And then we're talking about IoT devices, you're talking about cars, you talk about fleet management. If there's 1000 trucks delivering food and you're funding that vulnerability on that truck

*Adam Roth (24:46)*
and or trucking system, and you can shut down all the refrigerators while they're driving, you're going to cause really bad effects. And this last point about the heating system, if you watch Mr. Robot, people, not only did they control the temperature in the building through Mr. Robot, but they also were able to move laterally from the thermostat on the wall to other devices. And in a way, you can kind of do that with the Flip is Zero if that thermostat has a USB cable. So that's another whole story in itself. It's amazing.

*Joe Patti (25:20)*
Okay, so getting back to the Flip is Zero, took a little detour there. It can do something else that I find really interesting.

*Adam Roth (25:26)*
The Flip is Zero has a whole breakout on the back or the side of it, I'm sorry. And the breakout on the side of it has a listing for all the different pins, as well as voltage.

*Adam Roth (25:39)*
And what you can do is the radio is capable of receiving, but it might not have the right antenna or the right contacts. And when you plug this board in with these extra pins and wires, you can use a breadboard to enhance the current capabilities of the Flip is Zero to do other things. So let's say, for example, let's make this up, right? Let's say you're doing something outside the band of Flip is Zero. Let's say it's radar. You might be able to use a radar antenna to receive signals, send it back to the Flip is Zero and use that Flip is Zero as a computer and add programs or firmware to do additional testing or additional compromises.

*Joe Patti (26:27)*
Oh, that's what it's for. You can essentially then add different radios, different sensors onto it. Wow. That's pretty intense, actually.

*Adam Roth (26:38)*
So people who are currently doing that with the Raspberry Pis, in essence, what you're basically doing is you're kind of, instead of using a Raspberry Pi, you already have a completely built computer that you can carry with you and put a breadboard on it and do some really, do it yourself add-ons. The breadboards are about $10 each and they're actually, I'm looking at it, they're sold out

*Adam Roth (27:07)*
because you can do so much. There's so many people out there who are so talented, it could do so many things.

*Joe Patti (27:11)*
We have to be a bit of an electronic geek to know how to do that stuff, but there are plenty of people who know how to do it and who have been, frankly, building a lot of these things themselves.

*Adam Roth (27:20)*
Yeah. I'm looking at it now. They're basically doing like Wi-Fi modules and things that you normally can't read, because as a capability of using that firmware to do it, they're having a lot of fun.

*Joe Patti (27:34)*
Okay. So where does this thing actually come from? This Flipper Zero. It comes from a company. According to their website, they're based in Delaware and it is a number of people. I think they're like 40, 50 people. They did a Kickstarter campaign that was very successful a little while back. And you can... Well, you could buy it off their website, but they said they're sold out until I think, as of this recording, they said they're going to get some tomorrow, maybe.

*Joe Patti (28:03)*
You were able to sell it... Well, you were able to buy it on Amazon, but then Amazon decided to ban it, right Adam? Yes, they did.

*Joe Patti (28:14)*
And you actually got your hands on one, but you got it through an interesting place. Not directly. I guess through the secondary market, I suppose you'd call it.

*Adam Roth (28:26)*
No, this is actually a legitimate market. They're a partner of Flipper Zero, but I had to get it from France. And literally by the time I got it, it was already available.

*Adam Roth (28:39)*
I got it from a partner called, I believe, Lab401 in France. But by the time I received it, it was already more readily available.

*Adam Roth (28:49)*
On the Flipper Zero website, but Flipper Zero does have partners. But yes, there's a whole entire market, third-party market, where people are selling them for $1,000 each.

*Joe Patti (28:57)*
Is that largely because of availability, just because they're in short supply?

*Adam Roth (29:02)*
I think because there was a big buzz for it in countries like Brazil banned it. And everybody's seen their role of the internet, that the hype was there and people were all buying them. And now that most of the people who had that hype bought them, the supply is more readily available. So you create this whole hysteria about, I need it, I need it, I need it. And everyone buys it at higher prices, especially through third-party markets. And now the demand isn't as high.

*Joe Patti (29:35)*
It is kind of interesting because people were saying, "Oh, it's been banned by Amazon." And it was in short supply. You had to go overseas to get it. In some cases, and I'm sure there were people gouging it,

*Joe Patti (29:48)*
in terms of prices like they will for anything that's hot. I had also heard that the US Customs Agency had seized a shipment, but never said why, at least in what I was reading. And the interesting thing with all of this is that it makes it sound so exotic and James Bond and everything, but these are not illegal by any stretch, as far as I know. And I am not a lawyer, not even close.

*Adam Roth (30:13)*
So I think because the US Border Patrol was not sure what the device was, and it wasn't analyzed, and people thought it was a threat. They seized a shipment, but I think they released it. And Flipper Zero even posted, I think, on Twitter or somewhere that they're waiting for official response from the US Customs to understand the reasons why they aren't happy with it. But eventually they got released, and now there's no problem importing them into the United States. So people get scared. They see something. They think it's a hacker tool, and they go crazy.

*Joe Patti (30:46)*
That's right. And it is important to remember, these are tools to be used for good, to be used to protect yourself and to help others protect themselves too.

*Joe Patti (30:56)*
And even when you do find something an issue, there are a lot of ethical matters on, so what do you do? Do you just keep it to yourself? Do you tell the world? And I'll tell the world may not be a good thing. Without getting too much into responsible disclosure, like we were saying, typically you would want to contact the manufacturer and tell them, "Hey, there's a problem here. Please fix it." There are protocols that you can subscribe to that will say exactly the way you should do it, exactly the way the vendor responds, what to do if they don't take care of it. But this likely is going to become even more important than it has been in the past because

*Joe Patti (31:42)*
this has been going on for a very long time in software. Software vulnerabilities are very common. We know how to do it if you know Microsoft every month, every second Tuesday of every month since out there patches, and a lot of other places do too on similar schedules in a similar way. However, now, as we were saying,

*Joe Patti (32:03)*
computers and software are being integrated into more and more devices that we use every day, there are more vulnerabilities out there too, and they're becoming much more pervasive. So this is going to be a very interesting thing going forward. The day is coming very quickly, and mine have even been here at some point where, say, on your car, they say, "You need to take this thing because we need to fix it right away." Or even, "You'll go to start it, and it'll be just like your PC." It's like, "Wait a minute, I'm downloading an update. I can't drive for a few minutes." That's going to be fun.

*Adam Roth (32:38)*
Well, and that goes back to, and I know we always go in circles with some of the conversations because they always bring up more points. The more sophisticated a device gets, whether it's your car, your HVAC, anything, the more vulnerabilities are introduced with the advanced technologies, and it gets to a point where there's going to be plenty of tools out there. Make no mistake, the Flipper Zero is nothing new as far as tools go. You can buy different tools on the internet to do everything that the Flipper Zero is doing. However, the Flipper Zero is a nice, compact tool that is embedded. It makes it easier for most enthusiasts to test these.

*Joe Patti (33:26)*
That's right. Don't be fooled either. This is convenient, and it's in a nice package. It's not as easy as people think it is. You do have to have a little knowledge and put a little time into this to know how to use it correctly. It's not beyond the realm of anyone who's interested and has some time. Also, be aware that some of the videos you might have seen, I have heard that some of them may be staged, exaggerated a bit, a bit sensationalized.

*Joe Patti (33:54)*
Again, going and taking a device. One of the first times I heard about it, I joked with Adam when he said, "Hey, I can change my TV channel with this." I'm like, "Wow, you just bought the world's most expensive universal remote. Congratulations." Not everything is so spectacular with them.

*Adam Roth (34:10)*
I'm going to give you an example. If I go to read your card that you have,

*Adam Roth (34:17)*
your credit card with the Flipper Zero, and I get your credit card number,

*Adam Roth (34:23)*
and then I go to buy something online as most websites, but not all, require security code. That security code does not get read by your card or by the Flipper Zero.

*Adam Roth (34:35)*
The card is imprinted on your card, the number. You're not getting that when you read it. If you need the security code, reading the card is not going to do anything for you. I want to make that clear. If you read somebody's bank card, you still need to know their PIN,

*Adam Roth (34:52)*
unless you're using it as a credit card and they don't require the security code.

*Adam Roth (34:56)*
There are staged things on the internet that make it seem like you can open up the gates to heaven with this, which I haven't tried yet.

*Joe Patti (35:07)*
That's because card skimming and things like that, they're nothing new.

*Joe Patti (35:13)*
Banks and all have been building systems around this for a long time. Don't get too scared by it. Don't think it's too easy because it isn't, but you can learn quite a bit and understand your vulnerabilities.

*Adam Roth (35:27)*
Yeah, the last thing I'm going to say is this in essence, and I know you're going to define what I'm saying, but this in essence has become the script kitty of pen testing physical tools.

*Adam Roth (35:39)*
It makes it easier for a person who's never done this technology before, but it doesn't make it like plug and play instantly. You know what to do. It requires a little bit of work, a little bit of studying and understanding. If you've never used these type of tools or pen testing, you still need to learn.

*Joe Patti (35:59)*
Yes, and I'm sure you can, but don't think it's too simple. Script kitty is a security term for someone who doesn't really know security, doesn't really know how to hack or to break into things or to test them and just finds a script or a program on the internet to run it. If it works, it works. If not, they're done. It's the lowest level and they were typically kids in the past. Although unfortunately some of those kids have grown up into very good and very troublesome adults, but please don't be one of them.

*Joe Patti (36:34)*
In any case, Adam, it is time for last call, but we have a very special last call today. We're noting that although it's last call here, we're going to have an after party.

*Joe Patti (36:47)*
And what we're going to do is we have a flipper zero. Adam has one in his possession and he is going to do an unboxing of it and show it to you on video. So after all this talk, you can get an idea of what this thing actually looks like.

*Adam Roth (37:02)*
So yeah, the unboxing is three minute round, one minute off. We'll get some most points wins. Oh, that unboxing.

*Joe Patti (37:09)*
I'm sorry. Not actual boxing. Yes. But unboxing. Yes. So a lot of fun. We will have that on our YouTube channel where you can also catch this podcast. And of course you can get the podcast on just about any podcasting platform of your choice.

*Adam Roth (37:25)*
And we're looking for feedback. We're definitely looking for feedback. So if there's something that you liked or didn't like, or you want to see something else or hear about something else, please email us at feedback at security cocktail hour.com. Again, feedback at security cocktail hour.com. And if you want to send this hacking tools to evaluate, Hey, we'll take them too. Yes. Thank you.

*Joe Patti (37:50)*
All right. That's it for this episode. We will see you next time, Adam.

*Joe Patti (37:56)*
Good doing this with you as always. That's all folks. Take it easy.