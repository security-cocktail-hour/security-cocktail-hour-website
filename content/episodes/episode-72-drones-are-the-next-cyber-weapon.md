---
title: "Drones Are the Next Cyber Weapon — And We're Not Ready | Luke Canfield"
seo_title: "Drones Are the Next Cyber Weapon — Drone Security"
date: 2026-03-10T00:00:00-05:00
draft: false
guest: "Luke Canfield"
category: "Hardware Security"
duration: "1:28:04"
image: "/images/episode-072.jpg"
description: "Luke Canfield reveals war-flying attacks on financial institutions, cartel drone operations, and why security teams must start thinking in three dimensions."
platforms:
  youtube: "https://youtu.be/YKSxyI-m-PE"
  spotify: "https://open.spotify.com/episode/18TYWLjiLpqGX995iDmqdL?si=K4fZ2CQbSiijDeFKpZmXkA"
  apple: "https://podcasts.apple.com/us/podcast/security-cocktail-hour/id1679376200?i=1000754652084"
  amazon: "https://music.amazon.com/podcasts/d11e431a-f7b1-4bb0-8671-024afce9ade6/episodes/073a3578-3132-4cd7-880f-e4eb59610612/security-cocktail-hour-drones-are-the-next-cyber-weapon-%E2%80%94-and-we're-not-ready"
tags:
  - drone-security
  - war-flying
  - hardware-security
  - cartel-drones
  - faa-regulations
  - cybersecurity-threats
  - fpv-drones
topics:
  - "War-Flying: Drones as Airborne Hacking Platforms"
  - "Real-World Drone Cyberattacks on Financial Institutions"
  - "Cartel Drone Operations and Border Security"
  - "DIY Drone Building and the Attribution Problem"
  - "Drone Detection Methods: RF, Acoustic, Radar, AI"
  - "Ukraine's Impact on Drone Technology"
  - "FAA Part 107/108 Regulations and Enforcement"
  - "Drones for Disaster Response and Active Shooter Situations"
related_episodes:
  - "episode-70-securing-mars-rovers-and-space-stations-with-nasas-former-cio-renee-wynn"
---
Luke Canfield has been building, flying, and hacking drones for years. In this episode, he walks us through what's actually happening at the intersection of drones and cybersecurity — from war-flying (strapping a Wi-Fi Pineapple to a drone for aerial man-in-the-middle attacks) to the Mexican cartels that pioneered weaponized drone operations two years before ISIS, to the teenager who built a submersible drone in his backyard pool.

This isn't theoretical. There have already been real attacks against financial institutions using drones as cyber attack platforms. And as commercial drone delivery (Amazon, Walmart, DoorDash) goes mainstream, the attack surface is about to get much bigger. Luke explains why human cognitive bias — we don't look up — is the fundamental security gap, and why "security exists in three dimensions" should be every CISO's new mantra.

### What We Cover

- War-flying: using drones as airborne hacking platforms
- Real-world cases of drone-based cyberattacks on financial institutions
- How Mexican cartels conduct 330+ drone airspace incursions per day at the US border
- DIY drone building: $200 and a 3D printer gets you an untraceable aircraft
- Drone detection methods: RF tracking, acoustic sensors, radar, AI/CCTV
- Ukraine's impact: how the conflict advanced drone technology by 15 years
- FAA regulations (Part 107/108) and fines up to $100,000
- Drones for disaster response: mesh networks, radio repeaters, wildfire fighting
- Active shooter response with FPV racing drones
- The coming Part 108 era and why a fake Amazon sticker may be the next attack vector

### Listen Now

## Full Episode Transcript

*Luke Canfield (00:00)*
it was in New York and they had a Wi-Fi pineapple strapped to a Mavic. And some guy looks out his window at like whatever financial building because these have all been done against financial institutions. The guy looks, some guy looks out his window, there's just a drone hovering outside of his window

*Adam Roth (00:04)*
I haven't. I'm just kidding.

*Joe Patti (00:05)*
⁓

Welcome to the Security Cocktail Hour. I'm Joe Patti

*Adam Roth (00:20)*
I'm Adam Roth.

*Joe Patti (00:23)*
Adam, this is gonna be the best day you ever had because today we're talking about one of your favorite subjects, drones. Excited?

*Adam Roth (00:32)*
I thought you could

I'm absolutely but I you were talking about how we use Gigamon with drones and do packet capture

*Joe Patti (00:39)*
Well, you know what? We might get there one day, but it's going to take a while. This is a hard subject and a very new subject. But fortunately, we have someone who really knows it and we're glad to have him on. We've got Luke Canfield. Luke, welcome to the show.

*Adam Roth (00:42)*
Yeah.

Yeah.

*Luke Canfield (00:56)*
Thank you, appreciate being here.

*Joe Patti (00:57)*
it's great to have you. We were just talking before the show, and Adam is super into drones, and I always like to talk about the security impacts of new technologies. And there's just not a big community of drone security experts. So we're really glad you were able to join us.

*Luke Canfield (01:13)*
And it's basically brand new. it, couple years, like people started thinking about the implications of this, even though like, ⁓ bit of my reading and research, like it's kind of something we should have been looking at like 10 years ago. But it was like drones are toys. They're either toys or...

They're a $10 million piece of like Boeing or Northrop Grumman equipment the military has and there's like no way in between so we're not going to talk about.

*Joe Patti (01:43)*
Well, it's interesting. remember, I'm going to date myself, I remember when they started using those Predators I think back in like Desert Storm in the early 90s. And I remember when they said, it's a drone, it's a drone. I'm like, that's cool. And even then I was thinking it was going to be like a little toy and then it's like a whole big airplane. But that's changed. Now they are much smaller.

*Adam Roth (01:49)*
Ugh.

*Luke Canfield (02:04)*
Yeah, like they have some really big ones. have like the Global Hawks, which are huge. Like a full size airplane. They can stay airborne for very long time and now you've got ones that are like the size of like dragonflies.

*Joe Patti (02:19)*
Wow.

*Adam Roth (02:19)*
Yeah,

and that's an important distinction, right? know, people think drones, they think either, like you said, Luke, military level drones, which are probably drones based on biofuel, and then they have drones that are a little bit, you know, they can be smaller, they can actually be that big too, but they're more based on battery life and more law enforcement or centric towards doing specific things like.

farms and crops and you know maps.

*Luke Canfield (02:50)*
Yeah, they've they've niche down

a lot to various like it's not like a catch-all thing like you got the you got the Ag drones which do anything from spraying pesticides to shining UV lights at birds to them away from chicken farms. I was reading about that Japanese are doing that. To keep bird flu from spreading they have like these drones that basically have a disco ball that shines like

*Joe Patti (03:10)*
wow.

*Luke Canfield (03:18)*
UV frequency like that we can't see birds can't scare away pigeons. It attracts the pigeons that trying to like roost on top of the building and scares them off.

*Joe Patti (03:27)*
that I didn't know about. I guess that's very clever. And that's what a lot of this is about, people finding clever ways to use this stuff. But Luke, so you're a security guy, but you've done or dealt with or been into drones for a long time. How did you get into the whole area?

*Luke Canfield (03:45)*
So back in the day, I wanted to fly. I wanted to be a fighter pilot, but my vision is horrible. I went and got into poli sci, national security, all that in college. And the big thing I was interested in was conflict prediction, basically. I picked up a geography degree focusing in GIS and took a bunch of remote sensing classes.

This one grad student, I wish I could remember her name. Like a 400 level remote sensing course she came in and she had a, it's like when the DJI Phantoms came out and she had gone to Africa and used one to map open pit diamond mines and like made a 3D model of it. And I was like, okay, these things are cool. Like they're getting more accessible. If a 23, 24 year old woman from, she was from Ohio.

And go to Africa with one of these and maybe a couple thousand dollars total and like make these really detailed 3D maps that you can pull up on a computer and like go through. And I started thinking about the different uses for them, but ⁓ for college students, so I was kind of barred, but I still read about all this stuff. And I also was reading about like the novel uses like new technology that's going on in like.

*Joe Patti (04:40)*
you ⁓

*Luke Canfield (05:08)*
GWOT global war error. Like a lot of like the weird stuff that was like starting to come out of like DARPA and like the dookie dudes that work at think tanks that were coming up with ideas for like battlefield uses for technology. It in the National Guard. There's actually one of our captains was an engineering student up at Ohio State. And he had a whole use like idea for use case for using drone drones swarms with magnometers on them to circle a building to be able to like

*Joe Patti (05:26)*
you

*Luke Canfield (05:38)*
map out or hallways and rooms were based on the metal, the metal work of the building. And he was talking about that. think that like, this is all like 2013, 2014.

*Joe Patti (05:52)*
Wow, That's amazing.

*Adam Roth (05:54)*
all this is amazing. Like ⁓ from an architecture standpoint, from drones as a first responder, know, being able to provide immediate assistance, drones being able to lower or land with an AED or defibrillator, drones that are able to, you know, provide cell phones to people that are stuck on mountains, where regular helicopters and it's too dangerous.

It's amazing the purposes and things that can happen today.

*Luke Canfield (06:26)*
So like one of the things I'm wanting to get into, I'm actually the talk that I'm doing out in Denver with one of my friends who's really big into radio stuff like mesh-tastic, ham. It is basically taking that idea and making like airborne like mesh-tastic repeaters or ham radio repeaters or repeaters for other drones. Like you have like a disaster like Hurricane Helene down in North Carolina, which I actually drove through that night through that, like before it got bad.

*Joe Patti (06:52)*
you

*Luke Canfield (06:54)*
And I've driven through their sense the place is still pretty messed up. But I've like, I've talked to people that were like utility workers during that and they were using mesh tastic like ⁓ nodes and handhelds to like report the fuel levels that generators like trying when they're trying to boot the cell phone towers back up. The talk I'm doing out in Denver with my friend Evan is basically around how to use drones and radios for disasters.

*Joe Patti (06:57)*
Mm-hmm.

you

so they were able to take a bunch of drones and I guess send them out and create a mesh network because the cellular communication was out.

*Luke Canfield (07:30)*
that they didn't

do that they were doing it by hand while driving in their utility trucks and I was like yeah no to my knowledge the only place it's really used drones for

*Joe Patti (07:35)*
really? ⁓ wow.

*Luke Canfield (07:43)*
Like, Flying Signor Repeaters has been in Ukraine. And a couple of companies are researching stuff for pipeline inspection in remote wilderness areas. Like, they send the drone out and they have their radio repeater, like, mesh-tastic to communicate with. You have a drone mothership that has six smaller drones. It lands, they take off, communicates with them, they go inspect the pipeline, come back, and it goes back home.

*Adam Roth (08:12)*
I think we spoke about this right SDN with drones software defined networks Yeah, so mean that's amazing look ⁓ Let me let me just do a selfish plug ⁓ KC2MGX. That's my ham radio call sign. I ⁓ I'm always into ham radio. I'm always into amateur radio I've been into it for a long time and the things that they're doing now with radio and and ⁓ and drones is beyond amazing, but like I said before I

I know it's not the same, a physical aspect of it. Person was stuck on a mountain, they couldn't talk to anybody. They couldn't get a helicopter up there. A drone was a lot easier to fly. More of an industrial level enterprise drone. Boom, they drop the cell phone from there or they release it with a parachute. Now this person has the ability to do it, especially with satellite phones and ⁓ what's even better is what people don't realize is the Verizon outage.

If you had an iPhone, you were able to do text to satellite. If you had a Samsung S25 and greater, you could do text to satellite. If you had a Pixel phone, text to satellite. So if you have a good phone and you're stuck somewhere, and you're able to get it, or if you don't have a phone and a drone can bring you a phone, you're gonna be able to least text.

*Luke Canfield (09:33)*
Yeah, one of the things that I was looking at, ⁓ because all this stuff's available online for either free or very cheap, and it was the 40 millimeter grenade launcher tubes that the Ukrainians made. I mean, it's what it is, but it's just like repurposing military tech, which is like where a lot of art in the modern world came from, was military applications. It's just like, okay, let's not use it for.

*Adam Roth (09:48)*
You

*Joe Patti (09:49)*
Ha ha!

*Luke Canfield (10:02)*
lethal purposes. ⁓ But you can I was like playing around with this like, okay, I'm going to upsize a little bit to fit a it's like a p 25. Like, basically, it's a it's a radio repeater got the size of a red bullet like it can fit inside of a red bull can is like, okay, if I can fit it inside of this the parachute, I can load six of these on here instead of like loading. Six 40 millimeter grenades like the Ukrainians Russians are doing.

And just have this drone flying like a straight path over a ridge line or fly to a designated point hover. Drop out a repeater and keep going and you have an entire mesh network, the radio repeater network.

*Adam Roth (10:45)*
Nice. And how do they repeat his power? Solar?

*Joe Patti (10:46)*
That's clever. That's nice. Yeah.

*Luke Canfield (10:53)*
So, battery or solar this battery there. But I have a short shelf life if they're solar. There's to be a bit bigger, you probably actually have to use quadcopter like a landing system. I haven't really thought about this cause I was just thinking about this today while working on the talk for Denver. But they're like solar powered, like Meshtastic repeaters and like ham radio repeaters.

*Adam Roth (11:06)*
Yeah.

So we spoke about this a little bit like you know you put like You you you put like a little battery as long as you load it correctly just to keep anybody that's listening to this if you if you do have an faa 107 license and you're gonna put equipment on top of your Your your drone, please load it correctly and properly and and be careful and follow the laws but

If you load ⁓ an access point and you can power it either from the drone or from a battery, can you imagine you're flying outside a place, a location, and it's like emulating somebody else's SSID, and then now you're capturing people's traffic, and you have a cell chip in there too, in that access point, and now you're a man in the middle attack.

*Joe Patti (11:50)*
you

*Luke Canfield (12:10)*
Yeah, so like the talk that I did last fall, which I'm actually going to probably put a video that isn't constrained by time limits up probably tonight since I finished the slide decks right before this. It was basically using an LTE modem with a headless Kali instance, all the antennas on it, and either placing it into an orbit

And using it as like a war flying platform, which very quickly can turn into running man the middle attacks or evil twins rogue access points. And which like drone becomes the carrier for like that, like cyber attack payload. And they're like, I think there's been three incidents of that actually being used and all of them were. Caught because they were. Right idea, horrible execution.

Like they were kind of mookish about it. Like the one, I think it was in New York and they had a Wi-Fi pineapple strapped to a Mavic. And some guy looks out his window at like whatever financial building because these have all been done against financial institutions. The guy looks, some guy looks out his window, there's just a drone hovering outside of his window and like, they got caught. And.

*Adam Roth (13:14)*
I haven't. I'm just kidding.

*Joe Patti (13:15)*
⁓

Wow, that's not subtle.

*Luke Canfield (13:32)*
And

yeah, like they just spend the complete lack of subtlety. And the one that I use in my case study in my talk was I think it was Eastern Financial. And they like their network team, like they got into the server and everything, but their network teams like as a rogue access point here, like they did signal tracing, they went up on the roof and there's like a Matrice 600 with like.

Wi-Fi pineapple laptop on it battery packs

*Joe Patti (14:03)*
Just like parked up on the roof someone just dropped it in there.

*Luke Canfield (14:07)*
Yeah, they landed on top of the HVAC, which I'd be a good place to hide it if it was disguised as something that's supposed to be there and not like a Matrice 600, which is a huge drone. It's a very like a ten thousand dollar drone to like, and it's not so it was nothing subtle about this. And they just go upstairs like they go up on the roof of their building. There's like lots not supposed to be there, obviously. And those guys got caught.

*Joe Patti (14:11)*
Yeah.

*Adam Roth (14:16)*
Yeah.

I have a pineapple pager now by the way, the smaller form factor which we're supposed to put out. We didn't get a chance to put it out yet but a pineapple pager is a nice little piece of equipment.

*Luke Canfield (14:41)*
I actually was when I was out at DEFCON is I think I think was when they Showing it off before like one on sale and I look cuz I have like the the big one And I was like, that pagers a lot be a lot easier to attach to a drone than like this big square with like three antennas sticking out of it then I have to work on like how I want to modify the drone for ergonomics for all these antennas and everything else and the battery and like making a power jumper

*Adam Roth (14:51)*
Yeah, yeah.

*Joe Patti (15:09)*
Well, that's amazing that you've been thinking about that because this attack, I guess you've called it some war flying or the man in the middle stuff. Adam has been talking about putting a pineapple on a drone and doing this like, I think as long as I've known him for like 10 years or so. So it's like we've come full circle. It's finally possible Adam, just don't get caught.

*Luke Canfield (15:27)*
that's what

there's that. That's like when it first started getting talked about, I think it was a glitch tech. Which I don't know if he's still active anymore. He was on Twitter. I want to say he wrote for fired every now and then. Like, I don't know the guy. Like I just, I was researching this cause I've thought about this for years too, but it's never did anything with it until last year. And I was blessed with ample time and money.

*Adam Roth (15:29)*
I'm not gonna do anything illegal, I never will.

*Luke Canfield (15:57)*
But like the earliest I can see when talking about this stuff is like 2016, 2017, 2018. And then like suddenly like in the 2020s, like you have like three cases where people are getting caught doing exactly that with the Wi-Fi pineapple.

*Adam Roth (16:11)*
So nothing would surprise me Luke and Joe if this attack in Venezuela involved drones doing some offensive security. I, sorry. Yeah, yeah.

*Luke Canfield (16:24)*
Yeah, doing some E war stuff. ⁓ think

I saw like some. ⁓ Yeah, they alluded to it. didn't say what their means or methods were, but I do. Yeah, this could be completely made up. I might have came to me in a dream, but I when I was reading about everything in Venezuela, like I thought that I read somewhere from like the ground report from the Venezuelans. There's there are a lot of drones in the air.

*Joe Patti (16:28)*
Well, they did acknowledge that, kind of.

Yeah.

*Adam Roth (16:51)*
that would not surprise me and this is the this is the funny part it's like you know joe is probably sick at me but like you know i as you probably know i'm going for a doctorate and my doctorate is in you know cyber ethical warfare and what i have found is that there's no delineation between a cyber attack and cyber warfare and what we're doing these days venezuela was absolutely acknowledged as a hybrid attack how they did the hybrid attack i don't know whether included drones or not

There's people alluding to it and not, but what we have not come to is like what constitutes cyber attacks versus cyber warfare, what constitutes kinetic and those thresholds. So now we're in a very muddy area

There's no real treaties based on cyber warfare and that also brings in Drones because they're now though all these things are in the mix together. They're all connected now

*Luke Canfield (17:52)*
Yeah, it's like one of big things I was into because like I did a poli sci degree is actually international studies with the emphasis on intelligence analysis and national security when I was at WVU because I wanted to go do Intel for the government. And they weren't hiring for that at the time. They didn't want you unless you had a math degree or Russian. And.

*Joe Patti (18:14)*
you

*Adam Roth (18:15)*
Yeah, Janik

Aburupursky.

*Luke Canfield (18:20)*
Rogi, Niet, Vodka, Orsh. But the big one of the big things I was into and I actually wrote about a lot of this stuff and I wish I didn't have a corrupted computer because I wish I had all of my papers and not just a couple of them but like it's like getting into like gray zone warfare and like hybrid warfare and like doing these attacks and doing things that

*Adam Roth (18:22)*
you

*Joe Patti (18:23)*
Yeah, there you go vodka. That's what I know.

*Luke Canfield (18:44)*
or like legal treaties and like, are so new that like we don't know how to classify it yet and building attacks that stay below the threshold of like, static retaliation, like which is a big thing the Iranians do like through their proxies over in the Middle East, like the Houthis and I think I'm not even want to try to pronounce but there's an oil field attack in Saudi Arabia.

which the Iranians hit it with a cyber attack and then started hitting it with torrents and missiles. And it's like, well, what was the leading element? Was it the cyber attack or was it the kinetic aspect of it?

*Joe Patti (19:17)*
you

*Adam Roth (19:23)*
It is just, it is beyond amazing what is happening in our world today. And speaking of thresholds, know, there's been, least within NATO, in Article 5, Article 5, for those who don't know, is Attack on One, is Attack on All. And whenever NATO 5 is, I guess, discussed or brought for discussion by NATO,

What they talk about is whether or not I think I have something to do with NATO Article 4 about security threats. my country, was this NATO member ⁓ put in a bad position ⁓ from a security standpoint? And if it rises to that level for NATO Article 4, then the people that discuss NATO Article 5 talk about each time there's no real threshold. Did this rise to the occasion

where they were attacked. we talk about radiological, biological, chemical warfare, but we don't talk about cyber. And that's where all these different countries that are on, that are involved with Article 5, they all have different perceptions of what really is an attack. And we need better definitions because as we progress, we want to ensure that if somebody really does have to attack, because they feel they're threatened, that they don't decide, well, let's

You know, let's undo a dam and let the water flood into a village. We got to be very careful of how we move forward.

*Joe Patti (20:58)*
you

*Luke Canfield (20:58)*
like what

the Russians have been doing in Ukraine going back all the way to like the what was the maiden revolt main revolution like back in 2014 where they actually did cyber to physical attacks to shut down the power and does that warrant a kinetic escalation is like well the uh California power grid uh that was the Metcalf attack I wanted to be 08 or 09 and which was a physical

attack against infrastructure, but any more that probably have a cyber attack against like SCADA systems, what the Israelis and US attributed did to the Iranians with Stuxnet at that nuclear facility. say, Southern California's entire power grid just gets fried by something similar to what happened in Russia. They're going to be like second, third, fourth, fifth order effects, like

going to be high casualty offense that could possibly be more high casualty than it had just been a kinetic attack, would that warrant a kinetic escalation? Most people would say, yeah, but you are also getting into attribution and international law about like, does that actually constitute like kinetic retaliation?

*Adam Roth (22:18)*
And that goes full circle right back to the drones, right? If you're using drones that don't have attribution and you're using these drones to do from a cyber attack to a kinetic attack and they're destroying infrastructure, how do you show attribution? Somebody might have bought it off of Amazon. You just don't know.

*Luke Canfield (22:42)*
There's a thing recently, I think it was the Netherlands, where they had the drones harassing the airport. A lot of drones. ⁓ I'll have to send it to you, but there's actually like this one thing I found, was like kind of obscure news thing. was like drone stuff, unless it's like a big fiery spectacular thing, doesn't really make main news. You have to go looking for drone specific news sites.

But there's like a bunch of students from some university that actually tracked the drones back and followed them and their flight paths. And like did a bunch of analysis with the radar and. Brace them back to three Russian linked ships, which. The whoever the European version of the Coast Guard is over there like the Interpol ought to say that like throw out an agency like whoever does security for like boats and stuff over there.

And there were no drones on these three Russian ships, but like these this group of like students drove around tracking the drones. I think they even flew their own drones out to the ships to look around. And it's like, no, these drones are probably coming from the Russians because like all their flight patterns like indicate they're going back to this area of these three ships that are just kind of hanging out. And like they didn't know and all that. the ships were actually. Connected to a subsidiary owned by like a Russian.

tractor that actually does a lot of drone work, which I'm not going to try to pronounce.

*Joe Patti (24:13)*
⁓

*Luke Canfield (24:17)*
just like someone threw consonants on a page.

*Joe Patti (24:20)*
OK, well, it's interesting that they were able to track these things. mean, you just know, at least commercial drones, they're pretty noisy. They're not subtle when you hear someone buzzing in your neighborhood with it. But generally speaking, the smaller ones, I'm assuming they're stealthy, that they're hard to pick up on radar, that they're a lot quieter, I mean, especially at night. How do you even find these things?

*Luke Canfield (24:46)*
So

that's like a detection. ⁓ Like, drones have all sorts of complications with them, detection. Unless you're using like a very like small scale radar, which is just now coming out because of the stuff in Ukraine. One radar, if they're even picked up because they're made of plastic. ⁓ They're small. It looks like a bird if it even shows up. ⁓

They're hard to visually identify, which I think that's like an area that AI could be useful for for like tracking. And there's like different ways you could do this, because otherwise you're just going to be live tracking, which would be like taking like a CCTV camera and like running analysis, pixel changes like in like every third or fourth. Screencap. ⁓ And there's acoustics, which.

They've done in Ukraine, and I think we did a little bit of in Syria during the ISIS days. ⁓ We and air quotations of like using acoustic sensors, but which was adapted from like sniper detection in Iraq and Afghanistan. But the issue with that, if you're like in an urban environment, there's so much background noise you have to filter through that you're not going to hear the drone. But they've been doing a good bit of that in Ukraine with the acoustic sensors.

And then there's like radio frequency tracking, which I have a hack one RF ⁓ SDR laying on my desk over there. Actually, I just found it. Thank goodness. ⁓ And it's actually one of the more popular methods in Ukraine now for detecting drones that aren't the fiber optic like fly by wire ones. It is like looking for like.

different frequencies that are like on the like 900 megahertz, 433, 5 gigahertz, 2.4 gigahertz to like the different telemetry data the drones send off and like being able to like actually track that using a directional antenna. There's been like lot of advancements with that like it's usually like

people making it themselves, defense contractors are getting in on it now, there's like some expensive systems that look really flashy. But basically like hooking it up to like a Raspberry Pi or like some other computer. And it basically scans and like locks in on the direction that the drone is coming from based on those frequencies. Another issue, because I've been trying to do that because a lot of these people in Ukraine that are tracking drones using radio frequency are using just $30

$300 SDRs and like the Linux ⁓ instance, but the issues software defined radio. Yeah, it basically takes all the hardware components of a radio and runs them as software like. There you got you.

*Joe Patti (27:34)*
Sorry Luke, what's an SDR?

okay, software and find radio. Okay, got it.

And I'm guessing

it's a little tiny thing too.

*Luke Canfield (27:51)*
Yeah, ⁓ there's like little ones that are like the size of a cigarette lighter and then you got like the ones that are like the size of a deck of cards like this one.

And ⁓ SDR++ is one. The Linux distro that I like for it is is Dragon OS because it comes preloaded with all the SDR software suites or you can install them on any Linux instance basically. And I've actually been practicing trying to use room detection with that. But the problem here, cause I'm in an urban area.

is there's so many wireless access points that just just the background noise but if you're in like a remote location where there's no wi-fi points theoretically like i could go detect this using this equipment

*Joe Patti (28:34)*
Yeah.

Anyone who's done wireless work in a city, even if you're not doing IDS or anything, if you're just doing site surveys, I mean, you see like downtown Manhattan, any city, there's just SSIDs all over the place. ⁓ And it makes me wonder at some point, if we really do have Amazon delivering packages at one point, is whatever frequency is the drone use going to get just as noisy, just as thick, just as tough to pick out?

*Adam Roth (29:14)*
So yeah, I was going say yeah. So typically drones fly two ways for commercial drones. Without going into modifications, right? You have either cellular on board on that drone as a cellular card, and they're flying them. And sometimes those cellular cards are on private networks, like for whatever vendor it is, Verizon, T-Mobile.

*Joe Patti (29:39)*
Is that for control for flying the thing or is that like the payload it's sending? Both. Okay.

*Adam Roth (29:42)*
Both. No, no, no, no. They

can do that too, but built into a drone is either Wi-Fi control, typically in commercial drones, and correct me if I'm wrong, Luke, or it's cellular. If it's cellular, that vendor, that carrier can create a private network where it's not accessible by everybody else. It's encapsulated into his own network that's communicated. But what also drones do over a certain weight, and that's all commercial drones basically,

*Joe Patti (29:52)*
Okay.

*Luke Canfield (29:53)*
Mm-hmm.

*Adam Roth (30:11)*
Is that they have a ADS-B out. An ADS-B out is exactly the same as a plane. So when a plane is flying, they do ADS-B out. They let you know where that plane is on radar and stuff. The only thing a drone doesn't have, unless I'm wrong, is ADS-B in, where you can't ingest that there are other planes, drones near it. Yes, without going into specific vendors, there's a vendor out there that does identify drones and it does it very well. But...

But there are other people trying to get into the game to find other ways of doing it because it does know signatures of frequencies and how it operates and that's how knows the drone's coming. Because a drone flying is going to be different from a ham radio that's going to be different from something else.

*Joe Patti (30:56)*
OK, but that gets us into something else that I wanted to talk about. You're talking about, I look at that as similar to a phone or whatever. You're buying this stuff off the shelf. It's got some kind of identifier. You can track it and all that for the people who are being good. But Luke, from what I understand, when it comes to drones, you're very much in the world of, do it yourself.

build custom ones, can build custom gear.

*Luke Canfield (31:24)*
So, a lot of the laws and stuff coming out about, like, we need to make some cities ⁓ up north municipalities. I can't there's a 1 state out West. Utah, I think maybe don't quote me on that. But.

*Joe Patti (31:39)*
Well, if it's something

that's illegal, it's New Jersey is in there because everything's illegal here.

*Luke Canfield (31:44)*
I mean, your house property

taxes make everything illegal, but that's another story.

*Joe Patti (31:52)*
You know what? That's a good segue. We'll take a little break since you mentioned property taxes to talk about what we're drinking today.

*Luke Canfield (31:59)*
Yeah.

*Joe Patti (32:02)*
So Luke, what have you got? Because you called this one as our esteemed guest.

*Luke Canfield (32:07)*
got a Kentucky Mule because I didn't want to go out and get vodka to make a Moscow Mule. I also have a Moonshine Mule sitting here for when this is gone. But it is a Moscow Mule. Substitute the vodka out with bourbon or substitute the vodka out with moonshine.

*Joe Patti (32:25)*
You know, that's interesting because I've got here, and then I got this as a gift, some old Forester, a Kentucky bourbon that I've never had before and I actually like it quite a bit. ⁓ but we got some kind of Kentucky karma going on today. Adam, what have you got?

*Adam Roth (32:43)*
So ⁓ I chose not to go back out because it was snowing out. I ended up drinking shameless plug. I'm drinking whiskey in my security and mixologist academy cup, which is beautiful. That's the new core system that we're coming out with, but it's whiskey. So it's good. I'll send you one. I am going to send you one.

*Luke Canfield (33:01)*
That's a nice looking mug. Okay.

Well, I appreciate that. I love collecting coffee mugs.

*Joe Patti (33:06)*
Well...

Well, that's a cool mug at him, but you know, for the show, I think we need, if you're going to be drinking like, you know, alcohol or something, I think we need to invest in some glasses. Like we got this security cocktail hour logo, martini glasses, maybe we need some like that. You know, I feel bad seeing you drink, drinking liquor out of a cup.

*Luke Canfield (33:28)*
If you could get like a logo like a Moscow Meal Cup, or these copper cups, like that'd be kind of cool. Or like on a whiskey like rock glass.

*Joe Patti (33:35)*
Yeah, well the copper-

Yeah, that kind of thing. mean, the Moscow meal in the copper cup, that's totally acceptable. The coffee mug's a little weird. You seem like you're in an old private detective show, and you think the guy's having his coffee, and it's really at 9 AM, a bourbon or something.

*Adam Roth (33:45)*
So look at the... Yeah.

that's the whole idea,

but I'm doing product placement. But look, yes, we spoke before the show started and before that, that we're looking to have a long term relationship. So we're going to talk about what that design looks like for the glass. We'll come out with a glass. I'll send you the Academy Cup first, and then we'll talk about making some custom glasses so that when we, and my passion, Joseph has slapped me right now.

*Luke Canfield (34:13)*
Okay.

*Adam Roth (34:22)*
is to come out with our own one day, a security conference up in New York. I don't know if it's the end of 2026 or the beginning of 2027, but we'll have a couple of those classes where we'll raffle off or win the contest for that when we do that.

*Joe Patti (34:28)*
yes.

*Luke Canfield (34:38)*
That sounds pretty good. I'd love to come up for that. haven't been up to New York in 12 years, so, and I have quite a few friends up there, so it'd good to get them out to a conference, because they're all tech people too.

*Joe Patti (34:40)*
Okay. Wow. Definitely like to have you on.

Yeah, you'll like it. It smells like dope now. It's really cool.

*Luke Canfield (34:58)*
⁓

what? Last time I went there, it smelled like cold and sour mill down in Times Square.

*Adam Roth (35:07)*
Well...

*Joe Patti (35:07)*
Yeah, well, know, the city's

evolving. Times change.

*Adam Roth (35:11)*
Yeah, whatever the case is, it's still New York City. It's either gonna be New York City or North New Jersey. We'll have the conference and you'll bring those 12 people because we need as many people as we can get at the show.

*Luke Canfield (35:20)*
You

*Joe Patti (35:22)*
That's

right.

*Adam Roth (35:25)*
Yep.

*Joe Patti (35:25)*
Okay, so Luke, I interrupted

you. Where are I?

*Luke Canfield (35:29)*
Yeah, I made a joke about property taxes up in New Jersey. ⁓ yeah, DIY drones like drones being illegal and stuff like. Trying to get rid of the off the shelf drones. Unless you're dealing with like people of mookish behavior and temperament like the people that were hovering outside of a financial window on the 30th floor. Like Wi-Fi, pineapple. Those could be.

They have so much stuff in them like when I lived up in DC for years, like I couldn't even take like my Mavic Mini. I couldn't even get it off the ground because like a 50 mile like exclusion zone for like drones without getting like a very special permit to fly in that area because there's so much sensitive stuff up there. But for a couple hundred dollars on the low end, depending on what your intent is,

You can throw a drone together with like a speedy B or a Maytech like flight controller. And just fly it or program it, because you can program flight paths and all this stuff in into it using already pilot or beta flight. And there's no proprietary software on there like DJI or these other commercial drones have.

You actually have to be connected to the internet and have your phone connected to it and it has all your data you have to register you have to Depending on the size. I would have to register it with the FAA and you can just fly it without any Restriction

*Adam Roth (37:04)*
Restriction, yeah.

*Joe Patti (37:07)*
Okay, so you build one like that. Like you say, you get a flight controller, you obviously get batteries and all this stuff. And I know you can get the propellers, wherever, probably on.

*Luke Canfield (37:12)*
Yeah.

You

can print those off, can get them in like packs of four, eight, twelve off of Amazon for like twenty bucks depending on the size of them.

*Joe Patti (37:27)*
OK, so I've been curious. So OK, you're building an aircraft. And even if it's a small one. And I've always thought, maybe my thinking is out of date, that if you're building an aircraft, you've got to know something about ⁓ aeronautical engineering and all that sort of stuff. Do you or is it just like these controllers just expect to have something with four propellers and that's it?

*Luke Canfield (37:40)*
Mm-hmm.

Quad copters are easier than ⁓ fixed wing because

you're not dealing with the aerodynamics like a quadcopter like I saw a Russian quadcopter that was literally a tree log. Like a hollowed out tree log packed with kinetic stuff with like four propellers like jammed through it.

*Adam Roth (38:12)*
Yeah.

*Luke Canfield (38:14)*
All right, that's.

*Joe Patti (38:14)*
I think

I've seen that in Ukraine too. Don't they like build them in the field and they're just like they use a piece of plywood or whatever they got around? Something. Yeah.

*Luke Canfield (38:17)*
Mm-hmm.

Yeah, or PVC pipe, garbage, sheet

metal. Like, that's not very aerodynamic at all.

*Joe Patti (38:27)*
Okay.

*Adam Roth (38:27)*
Let me add Joe you can go online and literally get the The code to print out pretty much the whole entire a whole entire drone like a quadcopter It says use this to print all the pieces and then go online in all those parts and you're making a drone yourself without attribution to any one vendor it's

*Luke Canfield (38:50)*
Yeah.

*Joe Patti (38:52)*
you made a

3D printer you're talking about. Okay.

*Adam Roth (38:53)*
Yeah, 3D printing. yeah, not a,

*Luke Canfield (38:54)*
Mm-hmm.

*Adam Roth (38:55)*
not not a, not printing on a piece of paper and making a plane. So, um, so the point I'm making is they say, this is what you print, and this is where you order the parts on Amazon or on any special drone manufacturer, uh, that sells the parts. So it's that, or it'll say, go buy, go print this, go buy this GGA propeller, DJI propellers, go buy this, you know, radio, go buy this, and you're buying it, you're sourcing it all together.

and now you built a drone that 50 other people, 100 people already made.

*Luke Canfield (39:26)*
Yeah, and the crowd, like, it's like one of the big things like the whole talk I did, like calling it like the drone renaissance is like the crowdsourcing. Where like, you have like thousands, tens of thousands of people around the world who largely was driven by the FPV hobbyists, like the drone racing people.

*Joe Patti (39:27)*
wow.

*Adam Roth (39:44)*
First person view,

*Joe Patti (39:46)*
that's the glasses when you're controlling the thing. Okay, cool.

*Adam Roth (39:48)*
Yeah.

*Luke Canfield (39:51)*
And any design that isn't good gets thrown aside and what is what works is good and they just build off of those and a lot of the designs for like the kit bashed drones like printing off stuff and throwing it to the other parts like the stuff in Ukraine like I think in my opinion this is just completely my opinion is advanced the drone space like 15 years ahead of where it was two years ago.

*Joe Patti (40:19)*
Really? Wow.

*Luke Canfield (40:19)*
Like they've actually

designed new propellers to get a space. I take like a 12 inch quadcopter with the battery and attaching like a payload to it. Well, they've just like, when you're dealing with drones, like you're fighting battery life with thrust, with weight for like how far it can go. Well, they've modified and tweaked and made like iterative changes on the propellers to get those drones to carry more further.

than just a regular drone like a short time ago. It wouldn't be able to take off with that weight, but they've made new types of propellers and designed them and tested them and tweaked them like week by week until like it can do this new thing that they needed it to do instead of making a bigger drone. But

*Adam Roth (41:07)*
It will correct me from wrong. I think one drone Flew for 48 days, but what they did was that drone? was charging ⁓ was charging their batteries from a solar panel on top of the drone that allowed them to fly Constantly is that sound accurate or something?

*Luke Canfield (41:28)*
Yeah, I

read something about that. It was a fixed wing orbiter and I think the guy behind that, people behind it, I think they were engineering students. And that was like one of their previous concepts for like whatever they're doing for like their engineering department. And yeah, I think it stayed, I think it stayed aloft. It had really long wings. I wonder if it's the one I'm thinking of. And it was a glider and like.

It would get on the thermal drafts at night, stay in the air, and it's like a glider. It would like kill the engines to save power, sputter them back up, and during the day it would recharge.

*Adam Roth (42:08)*
And then there's other kids, made the drone, they made a drone submersible. That was really cool too.

*Luke Canfield (42:14)*
I saw

that and like everyone's like it just like I was told only DARPA was working on like drones that could go underwater and then you've got like I'm pretty sure the guy was a teenager too like I Yeah, I guess like 1617 and like he's in this pool in his backyard like this drones like underwater doing underwater drone stuff and it comes up to the top and it takes off and flies it was so cool and but

*Joe Patti (42:15)*
Hope.

*Adam Roth (42:20)*
Hahaha

Yeah, yeah, yeah, was a high school kid.

*Joe Patti (42:40)*
I'd love an underwater drone because I'll just tell you, me growing up in Jersey, going down the shore and everything, being by the water, there's lots of really interesting stuff down there. Especially in Jersey, you got guns, bones, and God knows what else, but it's pretty cool.

*Luke Canfield (42:52)*
They're up.

*Adam Roth (42:57)*
You know the kid's 16 years

old and he got recruited by some... Like, we'll put you through school. Yeah, yeah.

*Luke Canfield (43:02)*
his college is paid for.

I hope that guy's college is paid for.

*Joe Patti (43:06)*
Nice.

*Adam Roth (43:08)*
Well, it might

be paid for, but you might be working for a three-letter agency or the military at this point.

*Luke Canfield (43:14)*
I mean, the benefits are pretty good. I mean, if I was his age, it wasn't stupid and a teenager, go, yeah, yeah, that'd be great. It's like I got pension.

*Adam Roth (43:23)*
And

the irony is the biggest thing that they're talking about now with these UAO or aka UFOs is a lot of these UFOs that are flying in the sky they're also going submersible and And they claim this is where they're standing they're hiding so it makes it's kind of ironic right that This kid creates this submersible that can go in his pool come up fly and do that The applications are so military. I'm not saying it can't be anything else

*Joe Patti (43:24)*
Yeah.

*Adam Roth (43:52)*
but they're so military based. I mean, it's amazing what you can do with that, right?

*Luke Canfield (43:58)*
I guess kind of reminds me like the drone boats because like my brand of like neurodivergent autism stuff, it's like things that fly. I don't care about boats. I can't swim. I don't like the water. I was out in DEFCON. I talked to a couple of the engineers. I think it's Havoc who they're designing the drone boats. Like these are like from like 10, 30 up to hundred feet for the military.

*Adam Roth (44:19)*
Okay.

Oof.

*Luke Canfield (44:28)*
And they can do whatever you need, but like they have such a low profile and they're solar charged and they're deployed like in squadrons. Like they had like their whole booth there like showing like what they do. And like it's not like they're controlling like when they deploy a boat to an area, they're not deploying one boat. They're deploying like a squad, squadron of boats. And they can carry, they can carry cruise missiles, but they're telling me the cruise missile launch actually will destroy the boat, which makes sense.

*Joe Patti (44:48)*
okay.

*Luke Canfield (44:56)*
It can carry Navy SEALs in because they're telling me like their test group for their boats or former Navy SEALs who are riding them like jet skis, which they didn't design them for, but they're like, okay, that's an application. Or they can carry like quad copters or other munitions, electronic warfare radio stuff. But they're basically a bass boat or like a fishing boat with the bigger ones.

*Adam Roth (45:20)*
But that's, we talking about underwater, submersible, or above water?

*Luke Canfield (45:24)*
Right at the waterline like they're like they're like they're in the waves but like they could quickly That could quickly become like a submarine. I know the Australians actually employed a autonomous submarine that it was it wasn't small it's fairly big but it's still an autonomous underwater vehicle and Like I'm just thinking of like the shipwreck like explorers and stuff like the Titanic and like these other stuff like

*Adam Roth (45:26)*
Okay.

Because, yeah.

*Joe Patti (45:43)*
you

*Adam Roth (45:51)*
Yeah.

*Joe Patti (45:52)*
Hmm.

*Luke Canfield (45:53)*
Even like 20, 30 years ago, they were sending down like tethered, like, the immersive, submersibles with cameras and lights on.

*Adam Roth (45:56)*
Yeah, tethered, yeah.

*Joe Patti (45:57)*
Yeah.

*Adam Roth (46:00)*
Because that's the interesting part, right? You can't be autonomous and be submersible. They don't go together. You can be autonomous and submersible, but eventually you have to float a buoy or come up to the surface to get more instructions or to get communications. Because underwater, can't communicate. Unless I'm missing something. But you can bring an antenna close enough to the surface in order to communicate. So yeah, that's pretty cool, right?

*Luke Canfield (46:10)*
Mm-hmm.

And kid with the hybrid flying underwater one, I was actually talking to people back in December when I found out about it. Some of them were involved in engineering department. We were talking about how would we do this? it was like, well, you need a material that's waterproof. You're going to need gaskets and things to keep water from getting in, shorting out the motors. And you just go to Lowe's and get silicon sealant.

Like, however that kid did it, like, would like to find out how he did, because I would like to try to build.

*Adam Roth (47:00)*
I- I- he's-

*Joe Patti (47:01)*
I'd

love one of those just because it's so damn cool. That's awesome.

*Adam Roth (47:05)*
So I have a have a deck in the back of my house and the deck in the back of my house I wanted to clean it up when I bought the house So I had a guy that did steal and he actually welded some of the holes and everything But what he told me to get is there's a special marine sealant and that marine sealant that silicone It's better than almost every silicone you have the only issue is if you created a submersible

and you put the electronics in there and you seal it and it's 100 % seal proof, the only question I would have is how do you ⁓ dissipate the heat? Because you can't let the heat build up with electronics. So that's another issue in itself, right?

*Luke Canfield (47:50)*
But that's like back to the flying drones, especially like the quadcopters, they're more open so you have like air cooling, but a lot of like the fuselage is a fixed wing ones, you actually have to deal with heat buildup. Like there's there's like.

*Adam Roth (48:04)*
Yeah.

*Joe Patti (48:06)*
You

do? But they're all battery powered,

*Adam Roth (48:06)*
Yes, of course.

*Luke Canfield (48:09)*
Yeah, but they, the, the, the, broadcasting, like they get very, very hot. And you have to deal, you have to deal with like it not melting the plastic or catching on fire or melting the solder. You have to have good solder. But you have to like deal with like the ergonomics, the center of gravity of the aircraft. That way it doesn't just like fall out of the sky. So like when you're doing like fixed wing stuff, like you really have to like

*Joe Patti (48:11)*
they get hot.

*Adam Roth (48:15)*
Yes. It's radiation. Yeah.

*Luke Canfield (48:39)*
You can print out things to balance it, but you're usually balancing it by hand. And like you have, I have a food scale that I can measure stuff out on. So like, it's like, okay, because you're dealing with like takeoff weight, mean takeoff weight, payload weight and all that. And then you're also dealing with like the aerodynamics of it, but you also have to deal with like the heat buildups. Like a lot of these models, like you can just go one like Colt's 3D or Baker's World, printables, Thingiverse.

or any of the other STL sites. Like lot of these models, they actually have like ⁓ air channels in them. And there's like other cooling. There's like, there's other cooling things like running metal, ⁓ dissipate the heat. it's usual. Yeah.

*Adam Roth (49:14)*
Yeah, so they're cool through it. Yeah, they're cool through it.

*Joe Patti (49:15)*
Yeah.

*Adam Roth (49:26)*
even water going in and out of a tube inside the

device so that it gets cool by the outside as it comes back in.

*Luke Canfield (49:33)*
And that would make more sense to me, even though I don't really know anything about water drones other than my talking to the Havoc guys would be like, no.

*Adam Roth (49:39)*
No, no, meant

even the air, if you circulate the water inside, and it's still sealed, and it goes outside, the cooling of that water, I kind of had that with my pool, the op... Yeah, yeah, yeah, outside, yeah, yeah, so it's...

*Luke Canfield (49:44)*
Mm-hmm.

*Joe Patti (49:50)*
No, you've got to still exchange the heat somehow and get the heat out. Yeah.

*Luke Canfield (49:54)*
Yeah,

it'd be kind of like a gaming computer because like my computer right now has water cooler on it.

*Adam Roth (49:58)*
Yeah, exactly.

Exactly. Yeah, the gaming with the water cooler. But you know, the funny part, Joe, just so you know, is depending on how you fly a drone, the angle that you fly the drone, that changes the center of gravity and that also increases stall rates and then decreases stall rates depending on how you fly it. So if you're flying a drone and you're. And the quadcopters too, I don't know about the fixed wings. They could stall, yeah, depending on how you fly it. Yeah, absolutely. No, no, it's both. It's both.

*Joe Patti (50:17)*
You mean in a fixed wing or in those quadcopters in a... They stall? Really? ⁓ I thought that was a fixed wing thing. I guess not.

*Luke Canfield (50:22)*
They can.

*Joe Patti (50:28)*
okay.

*Luke Canfield (50:29)*
Anything that's airborne can stall out depending on the angle you're taking with it like the FPV racing drones Those guys amazed me I feel like I'm too old like really get into the FPV racing because like they have all the neuroplasticity that but like just go watching a YouTube video these guys racing them and they're doing like All sorts of like flips and barrel rolls and quarter eight roll with quadcopters

*Joe Patti (50:54)*
with quadcopters?

*Adam Roth (50:55)*
No, no, no,

yeah, the quadcopters, but the FPV quadcopters. The special one, they're a little bit different. Just so you know, Joe, the FPV quadcopters are used also by police and also by a military. actually, there are private companies now that hire FPV racers. So if there's an active shooter, they actually have these quadcopters.

*Joe Patti (50:57)*
Wow!

*Luke Canfield (51:00)*
Yeah.

*Adam Roth (51:25)*
stationary in a school and they fly them into the school to look for the active shooters. Yeah, you've heard that right Luke?

*Joe Patti (51:30)*
That makes so much sense. Yeah.

*Luke Canfield (51:33)*
Mm-hmm. Yeah, so I think in states out in the Midwest, I think it was like Minnesota or Wisconsin. That was where like one of those companies was like want to test that out. Because like the.

*Joe Patti (51:46)*
I would love

to see that deployed because I think that's fantastic.

*Luke Canfield (51:52)*
The FPV racing quadcopters, they're like 100 kilometers an hour faster. And that's only like, they could probably go even faster, but don't want to crash them. But if you don't care, then just kind of throw caution to the wind.

*Adam Roth (52:00)*
Yeah.

Yeah, typically law enforcement what they do is like more like the SWAT or the special What they do is they come up to a window. They break the window They put the FPV in usually usually these drones are the drones that have a protected propellers They have the propeller propeller guards. So if they do fly it in they hope not to like hurt anybody So they break their window they go in they fly

They go floor to floor by stairways or maybe into an elevator and they come up, whatever. Obviously you can't control elevators unless there's other ways I don't know about. But they go when they look for the active shooter, they look for the hostage taker, they do video and they get intelligence back through situational awareness.

*Joe Patti (52:48)*
No.

You see, I

really like that because, well, I got a whole other diatribe I can go on about, you know, school security. I got kids in high school, but you know, when they, the thing that immediately pops into my mind is that they do one of those shelter in places or something. They got an active shooter in the building. ⁓ you know, a thick can say, Hey, he's over on this swing. Everyone on this swing, get them out.

But I am no tactical expert, so we'll see what happens.

*Adam Roth (53:24)*
If you want, can enroll in the Luke Canfield class and you can become a tactical expert.

You

*Joe Patti (53:31)*
Well,

I'm definitely going to become a test student when Luke writes a class for us. That's, that's definite.

*Luke Canfield (53:37)*
It'd be great cause like I need to start working on that cause it's like, that stuff's gonna be in the fall. And I was like talking to someone who actually has ran workshops and courses. He actually makes a living doing it. And he was like, if you're wanting to do it in the fall, he's like, you need to have like this all done and planned out by like April at the latest. He was like, he's like, because like this he's like time goes by pretty quick with these kind of things. Like you can't just like keep putting it off like another week. So like, that's one of the things I'm

*Joe Patti (53:56)*
Wow.

*Adam Roth (53:57)*
Yeah.

*Luke Canfield (54:06)*
working on with like the whole Denver thing coming up.

*Adam Roth (54:09)*
I'm definitely interested if you do something after Denver and I would love to fly out, like I told you, and take a look at this. If you need my help, I'd be, love to assist you.

*Luke Canfield (54:18)*
I will definitely be in contact about that cause I could use all the help I could get for like, I'm, I'm, like the entire thing of like setting up like a village, these conferences, usually a CTF involved. So like, I'm trying to figure out like, what would a drone CTF be? I mean, you've got the forensic side of drones, but like, that's just a forensic CTF. You've got the OSINT side of drones, but that's just an OSINT CTF. Like, cause where drones kind of sit like at this like weird intersection of everything now. It's like, how do you,

*Adam Roth (54:45)*
Yeah, absolutely, yeah, yeah.

*Luke Canfield (54:48)*
Involve all of that and making a capture the CTF is captured flag. It's like a contest ⁓

*Adam Roth (54:55)*
like you

*Joe Patti (54:55)*
How do you also do that safely at a conference without drones flying all over the place? I have to do something.

*Adam Roth (55:00)*
it would have to be the truth.

*Luke Canfield (55:02)*
It had to be like simulated with like the data

because like there's also like you're getting to part 107 stuff with like FAA regulations and like, like how they did it at DEFCON is they had like these tiny drones and like a big basketball cage like you see like carnivals and stuff. ⁓

*Adam Roth (55:14)*
Yeah, yeah.

Yes, yes.

*Joe Patti (55:21)*
Really? Like the thing the guys ride the motorcycles in? That kind of thing?

*Adam Roth (55:21)*
Yeah

*Luke Canfield (55:24)*
Mm-hmm.

*Adam Roth (55:24)*
Like it's

almost like it's a square but it's MMA cage and what they do is they protect... Yeah, it's almost like that with the ceiling. as long as it's under .55, it's a hobbyist drone. You just gotta be really careful. You have have propeller guards and everything else. You can use the drone, maybe if it's like flying from one cage to another cage, you can use it to do SSID reconnaissance, do a...

*Joe Patti (55:29)*
it's one of those cages, okay.

Drone cage match. Alright.

*Adam Roth (55:52)*
red team caption this shit and come back, my language. But it's amazing what you can come up with.

*Luke Canfield (55:58)*
I mean, I've done my best not to curse on here because like every other word out of my mouth is usually an obscenity. So it's fine by me. ⁓

*Adam Roth (56:03)*
That was my one time. That was my one time.

*Luke Canfield (56:09)*
Yeah, that also gets like the part one or seven stuff people need to understand. Like there's so many rules and regulations. You can't fly over people. need propeller guards. You still have to stay under a certain weight, which one of the reasons like starting my own LLC around drones is like part one away coming out. I want to see about that.

*Adam Roth (56:27)*
my god, so a lot of these, it's on visual line of sight, he'll explain.

*Joe Patti (56:29)*
What's that, sorry.

*Luke Canfield (56:32)*
Yeah, like part 107 is for people like us. We want to fly a drone bigger than a Mavic Mini, like over 250 grams. And you can't go beyond visual line of sight. You can't fly over people. You can't fly under cars. It's like a lot of insurance. Anything resulting in over $1,000 of damages, you have to report to the FAA.

*Joe Patti (56:32)*
Okay.

*Luke Canfield (56:58)*
It's all self-reported. So it's kind of keeping honest people honest. However, another asterisk asterisk, the FAA will find the ever loving hell out of you, get caught doing something illegal. Like in the tens of thousands of dollars, it's not like a slap on the...

*Joe Patti (57:01)*
Okay.

in the tens

of thousands for flying a drone. ⁓ wow.

*Adam Roth (57:18)*
Yes.

*Luke Canfield (57:21)*
It is it.

It's not a slap on the wrist. Like there's one woman up around your all's way like New Jersey or New York. Who she I think I think she was a realtor and don't quote me about I was reading about this like a long time ago. So I've forgotten details. They find her almost a hundred thousand dollars. Yeah.

*Adam Roth (57:37)*
Per instance, it's yeah, it'd be

10k per instance. So if they caught you doing something and you did it, you did 10 house inspections in one day. And I'm paraphrasing, don't hold me to it. It could be like $100,000. Because, oh, you did 10 of them in a day? That's $100,000.

*Joe Patti (57:51)*
Yeah,

I've seen those online, you know, because like everyone else, I checked the neighbors houses out, out on Zillow and my friends to see what they cost. And you know, now they do like, you know, drone flyovers and stuff with the house to, you know, show how lovely it is and everything. And she got fined for that like a hundred thousand. my God.

*Luke Canfield (58:07)*
Hmm.

*Adam Roth (58:08)*
And even if it's under

the weight that you have to get licensed, because it's commercial, it automatically becomes licensable.

*Joe Patti (58:17)*
Really? Okay.

*Adam Roth (58:18)*
So if I was inspecting

my own house and I had a drone that was point like less than point five five pounds I go by pounds and I flew it over my house to check my roof as long as I didn't fly over somebody and you know It also depends on where you are New York City does not allow you to fly drones without having a permit from NYPD But let's say it's in a place where you don't require a local municipality Municipality permit and I flew it over my house. That's legal. But like if my neighbor says can you fly over my house? I'll pay you $100

We are made to make it such that going towards commercial and not supposed to fly it over somebody for a payment and whatever else.

*Luke Canfield (58:56)*
Yeah, there's...

*Joe Patti (58:56)*
Okay, so

the takeaway I'm getting from this is this ain't like slapping together a gaming PC. You can do whatever you want. This is like regulated stuff. You got to know the rules.

*Luke Canfield (59:05)*
You can slap it together,

you can slap it together, but if you do something that isn't kosher with like, or 107 or any of the FAA or FCC rules now, you're going to get fine. You're going to get fine really hard.

*Adam Roth (59:23)*
And they're an enforcement agency too, in a sense.

*Luke Canfield (59:25)*
Yeah, like during COVID during the lockdown, there's like a lot of people like, okay, we're locked down or have to be at home. I'm like, I'm going to fly my drone. This guy down Florida, I used to watch his videos. had like one of the parrot fixed wing drones. The one like he's just doing like landscape stuff. He's like flying down like an empty highway in the Everglades and the FAA had people going on YouTube and watching people's YouTube videos to see if there are any violations.

*Adam Roth (59:52)*
Yeah, yeah, yeah, yeah, yeah.

*Luke Canfield (59:53)*
and then going and find them and this guy got fined like $20,000. We're flying over an empty highway because YouTube, because it was technically monetized on YouTube, they considered it a commercial flight.

*Joe Patti (59:53)*
Really?

*Adam Roth (1:00:06)*
Yes.

*Joe Patti (1:00:09)*
well, we don't have to worry about that, Adam, right?

*Adam Roth (1:00:12)*
No, ⁓ first of all, I have no drone video online. And second of all, just, there are a lot of people that do the FPV, they show the tricks they're doing and stuff like that.

If you start making money from it, it's commercial. If somebody says I want to send you something to sponsor, fly my drone in this thing and you're flying the drone, you just got paid by using their drone.

*Luke Canfield (1:00:41)*
Yep. ⁓

*Joe Patti (1:00:41)*
Okay, well, like

we say with everything else, don't break the law. These things should be used for good, just like the hacking tools and everything else.

*Luke Canfield (1:00:51)*
It's like my presentation. I had like this big disclaimer on like the very first slide while I'm introducing myself. It's like, listen, hacking is cool and legal penetration. Like you have a statement of work agreement and SLA sign. You can hack all you want as long as it has like an entity or organization's permission. Don't go out and do illegal hacking.

Don't do illegal flying because you will end up in jail and there's like no wifi, the lighting's bad, the food's bad, the roommates are bad, everything's bad about going to federal prison.

*Adam Roth (1:01:27)*
And

you can't fly your drone out of the cell, you can fly a drone into the prison area and drop lobster.

*Joe Patti (1:01:34)*
And I can also tell you, if you get into prison and they ask you, what are you in for? And you say, illegal drone flying. I think you're in big trouble.

*Luke Canfield (1:01:34)*
That was wild.

Yeah, you're like, you're.

*Adam Roth (1:01:44)*
Not really! They might

tell you to bring their friends. Listen to what Luke's gonna tell you about the lobster.

*Luke Canfield (1:01:50)*
There was an incident back in December. cannot remember where it was. Was it up your all's way there, Adam? But they flew in lobster, menthol cigarettes, kind of candy. It's like, yeah, it's a carton of menthols, lobster, like a lobster dinner, ⁓ corn on the cob, and a bunch of just other random stuff like money and drugs. like, where they had like,

*Joe Patti (1:01:50)*
Okay.

*Adam Roth (1:01:56)*
I don't remember where it was, but it was freaking hilarious.

into a prison here.

*Joe Patti (1:02:05)*
into a prison.

You sure this

wasn't Goodfellas? Because like, you know, you see that scene when they're having the dinner and everything.

*Adam Roth (1:02:20)*
It was good fellows in a sense, but it's not-

*Luke Canfield (1:02:22)*
Yeah, I was gonna say, in a sense it was. A lot of these prisons, they'll post the pictures, like the contraband they collect, like a lot of police agencies do, when they have a big drug bust. But you have lobster tails, menthol cigarettes, snack cakes, and money and drugs.

*Joe Patti (1:02:25)*
Yeah.

*Adam Roth (1:02:42)*
In December 2025, a drone attempted to deliver a surf and turf holiday meal, including raw steaks, crab legs, and Old Bay seasoning to inmates at the Lee Correctional Institution, no, South Carolina.

*Joe Patti (1:02:42)*
Wow.

*Luke Canfield (1:02:50)*
It was in Maryland. It was in Maryland. I guarantee that was in Maryland.

No. He mentioned Old Bay, yet it's Maryland. Automatically Maryland in my mind.

*Adam Roth (1:03:01)*
So now it's a misdemeanor to fly a drone near a prison punishable by 30 days in jail.

*Luke Canfield (1:03:07)*
It's actually kind of wild to me because ⁓ the contraband's like, okay, that'd be drug smuggling, which makes it a felony or something. There's one book that I read, I was down in Dallas back in December for like, buddy of mine got married and I was like, didn't want to get a hotel room for like another day. So I got, basically was hanging out in Starbucks until like there was like the wedding reception and going to the airport. ⁓ And this.

book was amazing to me. It is called The Criminal Drone Evolution Cartel Weaponization of Aerial IEDs and

*Adam Roth (1:03:40)*
That's a mouthful.

*Joe Patti (1:03:40)*
That's

a mouthful. Okay, yeah.

*Adam Roth (1:03:41)*
Yeah, you said the same thing, yeah.

*Luke Canfield (1:03:43)*
I mean,

the people that wrote it were like DEA academics, drone people also, but like it's an interesting read. so it was really quick read because I read it in like eight hours because I had nothing to do for eight hours. But like a big thing they're talking about is like the cartels actually pioneered a lot of like what we're seeing with the drone stuff. It's like, ⁓ like everyone attributes ISIS over in Syria. They're the first group to use a weaponized drone. Actually, it was the the NOLAs and the Zetas.

*Joe Patti (1:04:02)*
Yeah.

*Luke Canfield (1:04:12)*
Two years prior to ISIS and a lot of the stuff in Ukraine It was attributed to like all the Ukrainians came up with this first actually no, it was the Mexican drug cartels and like

*Joe Patti (1:04:22)*
Are you kidding

me? That I did not know. Is that right?

*Luke Canfield (1:04:25)*
It's

like one of the things that's like, should be bigger news here in the States because like, I can walk to Mexico. Like I'm in West Virginia right now, but I can theoretically walk to Mexico. It's going to take me a long time, but I could do it. But I have a slide set from the thing I'm going to throw on YouTube later.

*Joe Patti (1:04:29)*
Yeah. ⁓

*Adam Roth (1:04:29)*
Date, yeah.

US Border Patrol

reported that the Mexican cartel flies their drones over the border to harass and then ⁓ bother the Border Patrol.

*Luke Canfield (1:04:54)*
while I'm thinking about this, it's like, I'm reading this now. Like the Mexican cartels, there's like been 60,000 reported drone flights near the border in just like quarter two of 2024 and like quarter one of last year, 2025. And it's like, this is just the ones that are detected, but it's like averages like it comes out to like 330 like airspace incursions a day from Mexican cartels across the border. And

*Joe Patti (1:05:18)*
⁓ that's amazing.

*Luke Canfield (1:05:22)*
One of the interesting things is because Border Patrol down there has been using ⁓ tracking them with radio frequencies because it's out in the middle of desert. There's no wireless access points, including the airwaves. So there was actually the first reported incident in December of the cartels using a fiber optic drone to cross the border. And most of these are like flying mules carrying drugs on.

⁓ Even though like the cartel has been using drones to kill each other for like over 10 years now

*Joe Patti (1:05:59)*
have.

*Luke Canfield (1:06:01)*
Yeah, again, this book is a great read. Like, they... I... I... I... I... I didn't know about this stuff until I was reading it there last month. Like, I've been into drones for years.

*Joe Patti (1:06:04)*
Never hear about this stuff. And you know, I actually read a book every now and then. Wow.

*Adam Roth (1:06:16)*
Crazy stuff.

*Joe Patti (1:06:17)*
That's wild.

*Luke Canfield (1:06:18)*
Yeah, it's like the cartels like have done a lot of stuff with drones that we don't think about.

*Joe Patti (1:06:25)*
Amazing.

*Adam Roth (1:06:26)*
Whatever is based on money, people are motivated.

*Joe Patti (1:06:30)*
So

*Luke Canfield (1:06:30)*
And a drone is easier than a guy sneaking across the border who could steal the stuff, run away with it, though they'll probably hunt him down and take care of him. This flight across the border gets picked up by someone, one of their guys on our side, and the drone either circles back and goes home. To the point they're actually designing their own fixed wing drones that just like drop off like a bag of contraband with like a parachute or something, or just drop it with gravity and pick it up.

*Adam Roth (1:06:59)*
They got the money to do the research and development.

*Joe Patti (1:07:01)*
That's crazy.

*Luke Canfield (1:07:02)*
But they make

*Joe Patti (1:07:02)*
Wow.

*Luke Canfield (1:07:03)*
their they make the cartels make their own submarines. They hire naval architects, they hire naval architects to make submarines down there like that's what they moonlight on. So like a drone is a lot simpler than making a man submarine.

*Adam Roth (1:07:06)*
Yeah, I know that, yeah.

*Joe Patti (1:07:07)*
Yeah.

Wow.

Well, you I think we could keep going on for quite a while. There is so much here and this is a really fascinating ⁓ whole world of what's going on.

*Luke Canfield (1:07:31)*
mean,

anytime you want to bring me on and talk about this stuff, I can talk about this ad nauseum, so.

*Adam Roth (1:07:36)*
Yeah, it's gonna be a part two.

*Joe Patti (1:07:36)*
I was going to say, Luke,

you got to come back. We got to talk more. This is, this is some great stuff. Thank you.

*Luke Canfield (1:07:44)*
And like there's a lot of stuff that I didn't even touch on, like looking through my slides and like getting off on tangents.

*Joe Patti (1:07:50)*
Well, I know you've got a lot of slides and you know what? We're going to give you a plug. We'll have it in the description. Luke has a great talk on YouTube and some great slides that are just absolutely fascinating and we didn't even get to it. There's just some great, great stuff there.

*Luke Canfield (1:08:08)*
I'm hoping to get the

better version of my talk online because I did the one on YouTube that I put up that you guys watched. That's the 30 minute version that I, because I only have like 25 minutes to speak when I was in Deadwood in October. And I did that like two hours before I drove four hours to the airport down in North Carolina from West Virginia to fly to Deadwood.

So that was a rush job. So I'm trying to put a bigger, longer version out on YouTube. I'm hoping to get that up tonight.

*Adam Roth (1:08:40)*
Is here a drone... Yeah. Is here a drone con yet?

*Joe Patti (1:08:40)*
Please do. I'd love to see that.

You

*Luke Canfield (1:08:45)*
⁓

there is, but I'm fairly certain that it is like around DC and like defense contractor oriented. ⁓ as I was talking to people and they're like, have a drone company, they're like, like you like the only person doing drones and like West Virginia with this stuff, like we want to work with you. And it was like,

I was like most of the people that work with drones are working for a three-letter agency in DC or down around Huntsville Alabama where like there's all the government R &D going on.

*Adam Roth (1:09:15)*
A lot of them go to my school. Actually, it's funny because my school concentrates on aeronautics, aviation, aerospace. And we were lucky enough to have a woman on the former CIO of NASA. And we spoke about some of these things too. So it's amazing.

*Luke Canfield (1:09:34)*
Yeah, it's like one conference I want to go to is down there at Cape Canaveral in Florida, Space Sec Con, I think it's called. And if it comes down between that and DEFCON this year, I don't know which one I want to go for. Because, yeah, it is like, they have it there Cape Canaveral there at the NASA Center and

*Joe Patti (1:09:52)*
I never heard of that one, but that sounds interesting just with the name.

*Luke Canfield (1:10:01)*
It is mostly focused towards like air and space. And then you got like the satellite security stuff. Those guys are wild to talk to.

*Adam Roth (1:10:08)*
We

had a couple of those people on too.

*Joe Patti (1:10:11)*
Yeah, you know what it immediately makes me think of, you know, reminds everyone, ⁓ you know, there is so much work and so much innovation and so much technology being developed and it ain't just AI. There's a whole other worlds of stuff going on.

*Luke Canfield (1:10:22)*
Forza.

God, I'm so sick of AI.

I'm sick of AI. I hate going to conferences and hearing another talk about like, ⁓ AI, agentic chatbot agent buzzword vomit of AI or enterprise business. I'm glad that's kind of like getting out of everyone's system because like in 2024, that was every talk at every conference. And it's like, okay, I'm not going to this conference. It's nothing but AI.

Even though I think AI, like I think we're in second Renaissance, to be honest, like that's like my big thing is drone Renaissance, but we're in a Renaissance in general with everything going on. But I was going to say, like getting into like the the hackery stuff, it's like the cleverness of like new technology and using these new innovative ways of using things.

Like AI for drones is going to be a big deal. Like Amazon is using AI for their drones. Like I actually think that you can even use it for your own drones. Like I have that bookmark somewhere. They have like an entire like AWS platform for drone control.

*Joe Patti (1:11:31)*
They do! ⁓ now that's interesting. Wow.

*Luke Canfield (1:11:33)*
⁓ It's in my book.

*Adam Roth (1:11:34)*
Yeah.

*Luke Canfield (1:11:35)*
It's in my bookmark somewhere. Someone sent it to me. I've been wanting to look at that. ⁓ I see.

*Joe Patti (1:11:39)*
Well, send it

to us. We'll drop it in the description for everyone. That's really interesting.

*Luke Canfield (1:11:44)*
it's like, yeah, like the, like the hacker aspect is like, okay. It's like, someone attached a wifi pineapple to a drone. Okay. That's neat. But is that really that big of an issue? Well, five years ago, it wasn't, but as drones become more common, we're going to be seeing drone like a Walmart, Amazon, even like Grubhub, Uber Eats, DoorDash. They're all working on drone delivery.

And once it takes someone from copying a drone or not even copying it, because like, one of the big things to talk about is how drones get past human bias and like, are limited like, senses and abilities. Like, birds have excellent eyesight. I have lost birds. I've lost drones to birds before.

*Joe Patti (1:12:33)*
I'll bet,

*Luke Canfield (1:12:34)*
because they can see a drone flying in their territory from a mile away. Like we have a hard time tracking anything moving 50 feet in front of us. And that's before you throw in cell phones, cars, background noise, whatever's on someone's mind through work day. Or is a person gonna be able to see a 12 inch object moving at 60 kilometers an hour, 500 feet up carrying a wifi pineapple? Probably not. They'll be lucky if they hear it.

*Joe Patti (1:13:01)*
Yeah.

*Luke Canfield (1:13:04)*
Because after you get like above 150 feet, you can't really hear them that well unless it is perfectly quiet. This is like, and birds aren't subject to cognitive bias. Like it's like, oh, no one's going to use a drone. I had like one guy argue with me once that, oh, drones, like no one's doing this with drones. It's going to be a guy with a laptop sitting out in the parking lot with his car. Well, if you have a security, you have security guards who are worth anything.

They're going to notice, hey, that car has been parked out there for a while and that guy's been sitting in it all day and we don't know who he is. Or this guy's been walking down the street back and forth in front of this building and has antennas hanging out his backpack. We don't know who he is. That's going to be quickly noticeable. How many people are going up and checking the roof to see if there's like a Matris 600 parked on top of the HVAC unit? Which was completely unnecessary. They could have had like a smaller one.

Disguised it as a weather station implanted on the roof and it looks like piece of the infrastructure, sprayed like rattle can it to where it blends in with the roof. You can go on Google Earth and see what the roof looks like.

*Adam Roth (1:14:10)*
I'll tell you this, I have seen people using ⁓ cameras on their roof, using AI to detect ⁓ objects. whether it's a pert... What? Yeah, yeah, yeah, yeah. So the whole idea behind AI is to know ⁓ direction of flight, it's to know crowd gathering, it's to know... So direction of flight is used in...

*Luke Canfield (1:14:23)*
Good. Good.

*Joe Patti (1:14:37)*
you

*Adam Roth (1:14:40)*
airports if you're going out the inn That's how they detect people that should be exiting the controlled area to the non controlled area from a flight from a gate into the general population crowd whether or not something's there Idling whether something's been there for a long period of time if exceeded a certain amount of time So there are buildings in New York City, especially that do have AI Enabled cameras on the roof looking for these type of things

I'm sure they're not as populated as they should be, but the reason why I can say that is I've been involved in some of those things at some point in my life.

*Luke Canfield (1:15:17)*
It's like where I'm at, like one of the nicknames for the area that I'm in is the Chemical Valley because there's all these chemical factories down the Ohio Valley, like the Canal River Valley, going out to the Ohio River through Charleston and Huntington. And like one of the case points I made is like ⁓ this is one chemical facility, I think it's Dow or DuPont.

And it's like they have amazing physical security at ground level. They have vehicle checks coming in, check ID. If you're not supposed to be there, they're not letting you through the gate. They're going to turn you around, send you back if they don't detain you and call the cops on you. But there's all of these chemical derricks on their own private property on this island out in the river because it's not a small river. And it's like, I know those factories have been there for decades. My grandfather used to work at one back in the 60s.

that those facilities are old. Do they have the security cameras facing inward on top of those chemical derricks? Like you land a drone with a solar panel on it, like one of those Russian Zadons with like ⁓ signal equipment on it. Are they going to notice that there's something up there that's not supposed to be there, like it flies in at night or something?

*Adam Roth (1:16:33)*
Yeah.

*Joe Patti (1:16:34)*
Yeah, that's something big I'm getting from this discussion and actually getting from your talk also that I saw. it's funny when you say you talk about, you know, the cars and we notice things, whatever, we do live in a three-dimensional world, but we largely exist on the ground and see things on the ground. And now with drones, things have become much more three-dimensional. We got to worry about the sky now.

*Luke Canfield (1:16:48)*
Yeah, I ⁓

It's like, yes,

security exists in three dimensions. I make fun of Midwesterns all the time, but they don't have a Z-axis. Again, I come from the mountain state. It's just like, you can be driving down the road and 500 feet to your left is like a sudden 1,500 foot incline. is, you kind of become aware of that elevation. Elevation's a big deal.

And was there something above me watching me? you're not used to looking up, then you're not going to think about it. what I was like the other point I was getting back to a bit ago is like the drone delivery is going to be so commercialized like part 108 and all the government incentives to commercialize drones. Like, so part 108, I didn't finish that one either. These two will tie together.

Part 108 is for commercial use and beyond visual line of sight, meaning you don't have to have a ground observer. You can fly it beyond the horizon.

*Joe Patti (1:17:52)*
Alright.

*Luke Canfield (1:17:53)*
With all these delivery drones, what's to stop a bad guy from slapping an Amazon sticker down the side of like their malicious drone and people are just, it goes back to the cognitive bias thing, are always an Amazon delivery drone, nevermind that it's parked on the roof of hospital or some piece of critical infrastructure or a VIP's residence.

Because it also gets into executive protection also, it's not just critical infrastructure and financial institutions, like you get into like, targeting of like VIPs.

*Joe Patti (1:18:26)*
Yeah, now you've got to protect your airspace. And if it's a VIP who has some money, it could be a very large airspace on an estate or something of that sort.

*Luke Canfield (1:18:36)*
And it's like one of the things like they're trying to pass now with the laws, I think it's Senator Lee, Senator Cruz and Senator Capito, who is my senator. Is trying to give legal rights to people's airspace, which we don't have. And this bill I don't agree with because it basically makes flying drones. Legally impossible to do.

as I interpret the bill.

Because right now you don't own your airspace and that was DuPont versus the EPA that was determined back in the 80s, I think.

*Joe Patti (1:19:12)*
I could easily be wrong, but I actually thought that was a much older concept. Going back to the earlier days of flight to say, you know, the government will control the airspace. It's like the airwaves. You don't own the airspace above you. Otherwise, aviation would be impossible.

*Adam Roth (1:19:28)*
Well,

it gets a little more complicated. ⁓ In New York City, a lot of buildings communicate via FSO or free space optics. Or they use ⁓ cell towers. And what people do sometimes is there might be two buildings communicating with FSO or free space optics, and they shoot the signal over somebody else's building. They do that now in New York City. The problem is if somebody builds up and breaks that connection,

Do they have a right to do it? My understanding is yes.

*Joe Patti (1:20:02)*
Yes, I understand that ⁓ they do. Yeah.

*Adam Roth (1:20:04)*
Yeah, but but but

but that's different from flying a drone over someone's property You really should not be flying a drone over someone's property. Also, that's another little story. But but the point i'm making is it's there's a delineation between Who do you ⁓ airspace rights over your building if you have a building? Is somebody allowed to shoot a signal above it and do they have any right to do that because now it's

going over their building, so whatever it is.

*Joe Patti (1:20:32)*
Okay, now we need a lawyer. boy. There is so much here. It's amazing.

*Luke Canfield (1:20:34)*
Yeah,

that is getting into stuff outside my space, which is like, I'm not a lawyer. can't speak to that. I'm not a government regulation corporate lawyer type. I have no clue about any of this stuff. I know that if I fly over someone's property above a certain elevation, which is like 10 feet above their property, including the top of their house, I'm legally allowed to do that. Excuse me, I'm legally.

There's nothing saying I can't do that. I usually like when I fly something like, and again, I'm out in the middle of nowhere, West Virginia for the most part, whenever I do this, I'll drive down the road until like Farmer Brown. It's like, Hey, we've known each other forever. Like the drone flying over your property at 200 feet. It's not the government spying when it's not you. Please don't shoot my drone down. Please don't take out your bird gun and shoot my drone down. And I don't need to do that, but

*Joe Patti (1:21:29)*
Yeah.

*Luke Canfield (1:21:31)*
And if he actually shot my drone down, it'd be a felony. For him.

*Joe Patti (1:21:35)*
But you know, we talk about all these laws and things and when you get to that, that's just being neighborly and everything, you know.

*Luke Canfield (1:21:41)*
Yeah, it's

like it's like a lot of this stuff. It's like, don't be a dick. Like, don't don't do anything blatantly illegal, like using a drone to hack something or fly it into something or there's been drone cases like peeping Toms. Don't be a pervert. Like, don't don't do anything illegal. And I think there's actually been some cases like paparazzi out in California, like where this is kind of like one of those spaces where it's like, okay, airspace the drone, like you're flying over someone's

*Joe Patti (1:21:45)*
Yeah.

fun.

*Luke Canfield (1:22:11)*
else in invading their right to privacy.

*Joe Patti (1:22:15)*
Okay, Luke, I'm gonna really date myself and we'll go out on this. This is totally retro. I don't know if you remember this, you had to be a kid, but back, I don't know, was the 80s, the early 90s or something. I think it was.

*Luke Canfield (1:22:30)*
I existed for

six months in the 80s. was born in May of 89. So I do not remember the 80s. I barely remember the 90s.

*Joe Patti (1:22:33)*
Okay.

All right. Well, if I remember this right, ⁓ Sean Penn married Madonna at some place, whatever, some big outdoor kind of thing. And the paparazzi, I don't think it was a drone at the time. It was a plane. And apparently he took out a gun and started shooting at the airplane. That was a big deal. So. Absolutely a felony. All right. Well, Luke.

*Luke Canfield (1:23:00)*
That's absolutely a felony. ⁓

*Joe Patti (1:23:08)*
This has been so interesting and so much fun. I gotta say, you gotta come back and talk to us more about this stuff. There is so much here. This is just great.

*Luke Canfield (1:23:16)*
Okay,

so the airspace determination between the EPA and DuPont was 1969. Yeah, so like that's been a thing for a while now.

*Joe Patti (1:23:25)*
Wow.

*Adam Roth (1:23:29)*
Cool.

*Joe Patti (1:23:30)*
All right,

*Luke Canfield (1:23:30)*
Yeah, and would love to be back on here talk about this because I mean, especially after Denver, after I get more information, like talk more about like the drones and radio repeating for disaster response, which I can even I can even talk more in detail about that for another episode alone on just disaster response because I lived through several disasters.

*Adam Roth (1:23:49)*
Definitely, so off the air, we're definitely gonna schedule a ⁓ post-conference ⁓ episode follow-up.

*Luke Canfield (1:23:59)*
I love that. ⁓

*Joe Patti (1:24:00)*
Yeah, and

as you go to the conferences, we'd love to hear about the latest and share it with everyone. There is so much going on.

*Adam Roth (1:24:04)*
You can even...

And if you're open to it, you can even take some video and we'll post it on our LinkedIn and YouTube shorts.

*Luke Canfield (1:24:13)*
Okay, absolutely. Every time I go to a conference, I run into new drone people who have some other interesting thing that's like, we can't all be doing the same thing at the same time. I was in line at DEFCON to get a t-shirt. There's 500 people in line, the line wasn't moving. The guy next to me, I started talking to him, he's like, oh yeah, I work for Tealdrone. And he was the guy that was telling me about the mothership drone coming down with the Laura on radio.

And you have like the little trends go out and spec the pipeline. I only know about that because I was standing next to the guy in line at DEF CON back out in Vegas back in August to get a t-shirt.

*Joe Patti (1:24:49)*
You know, that's how things go sometimes.

*Luke Canfield (1:24:52)*
And when I was up in Delaware, the Delaware B-Sides conference is absolutely amazing. It's a smaller conference. Like there's probably only maybe three, 400 people that show up, but just the quality of people that show up. And there's like people flying there from England, go to that conference. But like a lot of the information that I got from just hanging out in the radio village, were a couple of guys there from two different drone companies.

*Joe Patti (1:25:06)*
building.

*Luke Canfield (1:25:16)*
that dealt with drones for fire response for like wildfires and stuff. Like you have like these remote areas you can't get firefighters to that quickly. Well, they take drones down, drop like these big bowling ball sized like orbs filled with like flame retardant that burst in the air and it puts the fire out.

*Joe Patti (1:25:35)*
Really? ⁓ wow.

*Luke Canfield (1:25:37)*
And a lot of the parts that they're using to build their drones are the same parts that Ukrainians are building their drones with to attack the Russians. Because he was telling me they bought like a camera module from like China, because it's all made in China. That had preloaded like AI like target profiles for like attacking tanks. Like, because Ukrainians came up with this thing before like fiber optic went everywhere. And it was

If the drone loses radio signal with the pilot, it targets selects on its own. So if it loses contact like over like a bunch of Russian tanks that have like signal jammers on them, it will just fly into a tank and blow up because it has like the shape file, like in its like machine learning.

*Joe Patti (1:26:28)*
Well, that's cool

as long as it can accurately identify a tank. You know, that's the thing.

*Luke Canfield (1:26:32)*
Yeah, that's the other issue I

have with that stuff. like it's like $800 for that camera. they use that camera. They're buying that camera to put their drones together with. For drones that like, because it's an IR, it's a night vision IR hybrid camera. can fly at night and spot fires on the ground and drop a ball of fire be gone off. But it came preloaded with like shaped files like

Target recognition of like Russian tanks.

*Joe Patti (1:27:04)*
Luke, this has been so interesting. And I think I've learned more in the past hour or so we've been talking than really I've learned in a long time. Certainly more than watching YouTube videos. Not yours, of course. But ⁓ thanks so much for joining. And we definitely want to have you back to talk more. This is a huge, interesting world and moving really fast.

*Luke Canfield (1:27:29)*
Yeah, I appreciate being on here.

*Adam Roth (1:27:32)*
And I'll add to this, ⁓ like, subscribe, comment, ask questions. Let us know what else you want to hear and what else you want to see. And we're definitely going to keep in touch with Luke and we're going to provide ⁓ a lot more information. So thank you.

*Joe Patti (1:27:48)*
And if you've got

questions for Luke, please put them in the comments. We'll have a good discussion. Luke, thanks again. Adam, always good seeing you and everyone. Thanks for watching and listening. Take care.

*Adam Roth (1:28:00)*
Thank you.

