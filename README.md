# BibleBot
BibleBot is a multi-functional Discord Bot that quotes the Bible.

![GitHub issues](https://img.shields.io/github/issues-raw/cephox/BibleBot?label=Issues)
![GitHub](https://img.shields.io/github/license/cephox/BibleBot?label=License)
![GitHub release](https://img.shields.io/github/v/release/cephox/BibleBot)

# Content
- [Settings](#settings)
- [Invite Link](#invite-link)
- [Supported Languages](#supported-languages)
- [Contributing](#how-to-contribute)
- [Todo List](#todo)
- [API Reference](#which-api-is-used)

# How to quote the Bible?
The Bible can be quoted in any message by using following pattern:
```asciidoc
[Book-Abbreviation Chapter:Verse(s)]
e.g.
[Jn 3:16]
[Jn 3:16-20]
[Jn 3:17,20]
[Jn 3:17,20-23]
```
For example you can write `I like [Jn 3:16] the most because ...` and the Bot still is going the quote the Bible

---

# Settings
You can adjust the settings of the Bot e.g. prefix, language or bible translation
## Overview
To manage the settings you need to have Administrator permissions. Using `.settings` you get a simple overview of your current settings.

[![https://imgur.com/1GmGE6k.png](https://imgur.com/1GmGE6k.png)](https://imgur.com/1GmGE6k.png)

## Prefix
`.` is the default prefix used by the Bot. You can change it by sending `.settings prefix <new prefix>`

## Language
The default language is english. Change it by using `.settings language <new language (abbreviation)>` or `.settings lang <new language (abbreviation)>`
, dass du Te
To get an overview of all possible languages with abbreviation use `.settings language` or `.settings lang`

[![https://imgur.com/U24Fvd5.png](https://imgur.com/U24Fvd5.png)](https://imgur.com/U24Fvd5.png)

## Bible translation
The default translation is the King James version (kjv). Change it by using `.settings translation <new translation>`

To get an overview of all possible translation use `.settings translation`

**Note:** for each language different bible translations are available for you to choose from. Whenever you change the language, be aware that the bible translation changes automatically.

[![https://imgur.com/5MkmSeS.png](https://imgur.com/5MkmSeS.png)](https://imgur.com/5MkmSeS.png)

---

# How does a quote look like
[![https://imgur.com/c5vPjHs.png](https://imgur.com/c5vPjHs.png)](https://imgur.com/c5vPjHs.png)

---

# Invite Link
[Invite](https://discord.com/api/oauth2/authorize?client_id=689383347545440313&permissions=522304&scope=bot) the Bot to your Server.

It only required most of the read and write permission but if you want it to have permission to send Quotes to Admins-only Channels, you should use [this](https://discord.com/api/oauth2/authorize?client_id=689383347545440313&permissions=8&scope=bot) link.

---

# Supported Languages
- English
- German

---

# How to contribute
  1. Make a fork
  2. Contribute to your fork
  3. Make a pull-request
  
---
  
# Todo
- [x] Better help Command
- [x] Multi-Language Support (individual for Guilds)
- [x] Quote the Bible (using [getbible](https://getbible.net/api))
- [x] More Settings (like change bible translation)
- [ ] Acitvity cycle (Bible verses (english))
- [ ] Add Languages:
  - [ ] French
  - [ ] Spanish ?
- [ ] TTS Support

# Which API is used
The Bot is using the API from [getbible](https://getbible.net/api)
