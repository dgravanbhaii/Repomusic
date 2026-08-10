<div align="center">

# 🎵 REPOMUSIC

### ⚡ Powerful Telegram Music Bot

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=25&pause=1000&color=FF4D8D&center=true&vCenter=true&width=750&lines=🎵+Welcome+to+REPOMUSIC;🎧+Telegram+Voice+Chat+Music+Bot;⚡+Fast+%7C+Stable+%7C+Powerful;🚀+Built+by+@dgravanbhaii" alt="Typing Animation">

<br>

[![GitHub](https://img.shields.io/badge/GitHub-dgravanbhaii-181717?style=for-the-badge\&logo=github)](https://github.com/dgravanbhaii)
[![Repository](https://img.shields.io/badge/Repo-Repomusic-8A2BE2?style=for-the-badge\&logo=github)](https://github.com/dgravanbhaii/Repomusic)
[![Stars](https://img.shields.io/github/stars/dgravanbhaii/Repomusic?style=for-the-badge\&logo=github\&color=gold)](https://github.com/dgravanbhaii/Repomusic/stargazers)
[![Forks](https://img.shields.io/github/forks/dgravanbhaii/Repomusic?style=for-the-badge\&logo=github)](https://github.com/dgravanbhaii/Repomusic/network/members)
[![Issues](https://img.shields.io/github/issues/dgravanbhaii/Repomusic?style=for-the-badge\&logo=github)](https://github.com/dgravanbhaii/Repomusic/issues)
[![License](https://img.shields.io/github/license/dgravanbhaii/Repomusic?style=for-the-badge)](https://github.com/dgravanbhaii/Repomusic/blob/main/LICENSE)

<br>

### 🎶 Stream Music Directly Into Telegram Voice Chats

**Repomusic** is a powerful Telegram music bot designed for fast, reliable and interactive music streaming in Telegram groups and channels.

</div>

---

## 🌟 About Repomusic

**Repomusic** is a Telegram voice-chat music bot built for users who want a smooth music experience directly inside Telegram.

It provides:

* 🎵 Music playback
* 🎧 Voice-chat streaming
* 🔎 Music search
* 📋 Queue management
* ⏯️ Playback controls
* 🎤 Assistant account support
* 📡 Channel playback
* ⚡ Fast asynchronous processing
* 📊 Runtime monitoring
* 🔄 Restart/reboot support
* ☁️ Heroku deployment
* 🐳 Docker support
* 🖥️ VPS/local deployment

The project is maintained under:

**GitHub:** `dgravanbhaii`

**Repository:** `Repomusic`

---

# ✨ Features

<table>
<tr>
<td width="50%">

### 🎵 Music

* ▶️ Play music
* 🔎 Search songs
* 🎧 Audio streaming
* 🎬 Video playback
* 📋 Queue system
* ⏭️ Skip tracks
* ⏹️ Stop playback
* ⏸️ Pause playback
* ▶️ Resume playback
* 🔀 Queue management

</td>

<td width="50%">

### ⚡ Performance

* 🚀 Fast response
* ⚡ Async processing
* 📡 Voice-chat streaming
* 🧠 Queue handling
* 📊 CPU monitoring
* 💾 RAM monitoring
* 🌐 Internet monitoring
* 🧹 Automatic cleanup
* 🔄 Reboot support

</td>
</tr>

<tr>
<td width="50%">

### 🎤 Assistant

* 👤 Telegram assistant
* 🎙️ Voice-chat connection
* 🎵 Audio streaming
* 📡 Channel support
* 🔄 Multiple sessions
* ⚙️ Session configuration

</td>

<td width="50%">

### ☁️ Deployment

* ☁️ Heroku
* 🖥️ VPS
* 💻 Local hosting
* 🐳 Docker
* 🐍 Python
* 🔧 Shell setup
* 🚀 Startup scripts

</td>
</tr>
</table>

---

# 🎧 Architecture

```text
                    👤 USER
                      │
                      ▼
              ┌───────────────┐
              │   TELEGRAM    │
              │      BOT      │
              └───────┬───────┘
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
   🔎 Music Search          📋 Queue Manager
          │                       │
          └───────────┬───────────┘
                      │
                      ▼
              🎤 ASSISTANT
                      │
                      ▼
              🎧 VOICE CHAT
                      │
                      ▼
                🎵 MUSIC
```

The **bot** handles commands and user interaction, while the **assistant account** handles the Telegram voice-chat connection and streaming.

---

# 🎛️ Commands

## 🎵 Basic Commands

| Command        | Description                     |
| -------------- | ------------------------------- |
| `/start`       | Check whether the bot is online |
| `/play`        | Play a song                     |
| `/vplay`       | Play video/audio                |
| `/cplay`       | Channel playback                |
| `/playforce`   | Force play a new track          |
| `/vplayforce`  | Force video playback            |
| `/cplayforce`  | Force channel playback          |
| `/pause`       | Pause current playback          |
| `/resume`      | Resume playback                 |
| `/skip`        | Skip current track              |
| `/seek`        | Seek forward                    |
| `/seekback`    | Seek backward                   |
| `/stop`        | Stop playback                   |
| `/end`         | Clear queue and stop playback   |
| `/channelplay` | Configure channel playback      |
| `/reboot`      | Reboot from logger chat         |

---

# 🎶 Play Music

Use:

```text
/play song name
```

Example:

```text
/play Shape of You
```

You can also use a supported music/video URL where applicable.

---

# ⚡ Force Play

To stop the current track and immediately play another:

```text
/playforce song name
```

Also available:

```text
/vplayforce
/cplayforce
```

---

# 📋 Queue

When multiple songs are requested, Repomusic maintains the playback queue.

```text
Current Song
     ↓
Queue #1
     ↓
Queue #2
     ↓
Queue #3
     ↓
Queue #4
```

Use:

```text
/skip
```

to move to the next track.

---

# ⏯️ Playback Controls

### Pause

```text
/pause
```

### Resume

```text
/resume
```

### Skip

```text
/skip
```

### Stop

```text
/stop
```

### End

```text
/end
```

### Seek

```text
/seek <duration>
```

### Seek Back

```text
/seekback <duration>
```

---

# 📡 Channel Playback

Repomusic supports Telegram channel playback.

Configure it with:

```text
/channelplay <channel_username_or_id>
```

Disable it with:

```text
/channelplay disable
```

For channel playback, make sure the bot and assistant account have the required administrator permissions.

---

# 🎤 Assistant Account

Repomusic uses a Telegram assistant account for voice-chat streaming.

Configure the assistant session:

```env
STRING_SESSION=
```

Additional assistant sessions are supported:

```env
STRING_SESSION2=
STRING_SESSION3=
STRING_SESSION4=
STRING_SESSION5=
```

### ⚠️ Important

Never publish your session string.

A Telegram session string can provide access to the associated Telegram account.

---

# ⚙️ Configuration

Create your environment configuration from:

```text
sample.env
```

Example:

```env
API_ID=
API_HASH=
BOT_TOKEN=
LOGGER_ID=
MONGO_DB_URI=
OWNER_ID=
STRING_SESSION=
```

Optional additional configuration can be added according to `config.py`.

---

# 🔑 Configuration Variables

| Variable          | Description              |
| ----------------- | ------------------------ |
| `API_ID`          | Telegram API ID          |
| `API_HASH`        | Telegram API Hash        |
| `BOT_TOKEN`       | Telegram Bot Token       |
| `OWNER_ID`        | Bot owner's Telegram ID  |
| `LOGGER_ID`       | Logging chat/channel ID  |
| `STRING_SESSION`  | Assistant session        |
| `STRING_SESSION2` | Second assistant session |
| `STRING_SESSION3` | Third assistant session  |
| `STRING_SESSION4` | Fourth assistant session |
| `STRING_SESSION5` | Fifth assistant session  |
| `MONGO_DB_URI`    | MongoDB connection URI   |
| `UPDATES_CHANNEL` | Updates channel          |
| `SUPPORT_CHANNEL` | Support channel          |
| `SUPPORT_CHAT`    | Support group            |

---

# 🗂️ Repository Structure

```text
Repomusic/
│
├── 📂 ShashankMusic/
│   └── Music bot source modules
│
├── 📂 strings/
│   └── Bot strings
│
├── 🐍 config.py
├── 📦 requirements.txt
├── ⚙️ sample.env
│
├── 🚀 start
├── 🔧 setup
│
├── 🐳 Dockerfile
├── ☁️ Procfile
├── ☁️ heroku.yml
├── 📱 app.json
├── 🐍 runtime.txt
│
├── 📜 LICENSE
└── 📖 README.md
```

---

# 🚀 Deployment

## ☁️ Deploy on Heroku

### Step 1 — Fork Repomusic

Fork the repository:

**https://github.com/dgravanbhaii/Repomusic**

### Step 2 — Open Heroku

Go to your Heroku dashboard:

**https://dashboard.heroku.com/apps**

From there:

```text
Heroku Dashboard
       ↓
Create New App
       ↓
Connect GitHub
       ↓
Select Repomusic
       ↓
Deploy
```

### Step 3 — Add Config Vars

Open:

```text
Heroku App
    ↓
Settings
    ↓
Config Vars
```

Add:

```env
API_ID
API_HASH
BOT_TOKEN
OWNER_ID
LOGGER_ID
STRING_SESSION
MONGO_DB_URI
```

Add other variables required by your configuration.

### Step 4 — Deploy

Deploy the `main` branch.

Your repository already includes:

```text
Procfile
heroku.yml
app.json
runtime.txt
```

for deployment configuration.

---

# 🔗 Heroku Dashboard

<div align="center">

### ☁️ Manage Your Heroku Applications

<a href="https://dashboard.heroku.com/apps">
<img src="https://img.shields.io/badge/Open%20Heroku%20Dashboard-430098?style=for-the-badge&logo=heroku&logoColor=white">
</a>

</div>

---

# 🖥️ VPS Deployment

Install dependencies:

```bash
sudo apt update
sudo apt install -y python3 python3-pip ffmpeg git
```

Clone Repomusic:

```bash
git clone https://github.com/dgravanbhaii/Repomusic.git
cd Repomusic
```

Install requirements:

```bash
pip3 install -r requirements.txt
```

Configure:

```bash
cp sample.env .env
```

Edit:

```bash
nano .env
```

Run setup:

```bash
bash setup
```

Start:

```bash
bash start
```

---

# 🐳 Docker Deployment

Build:

```bash
docker build -t repomusic .
```

Run:

```bash
docker run -d \
  --name repomusic \
  --restart unless-stopped \
  --env-file .env \
  repomusic
```

View logs:

```bash
docker logs -f repomusic
```

---

# 🛠️ Requirements

Repomusic uses a Python-based music streaming stack.

Main technologies include:

```text
🐍 Python
📱 Pyrogram
🎤 Py-TGCALLS / voice-chat libraries
🎵 yt-dlp
🎧 FFmpeg
🎼 Spotify integration
🗄️ MongoDB / Motor
🌐 aiohttp
📊 psutil
🐳 Docker
☁️ Heroku
```

See:

```text
requirements.txt
```

for the complete dependency list.

---

# 🔐 Security

### 🚨 NEVER publish these values:

```text
BOT_TOKEN
API_HASH
STRING_SESSION
MONGO_DB_URI
HEROKU_API_KEY
SPOTIFY_CLIENT_SECRET
GIT_TOKEN
```

Do not commit `.env` files.

If a credential becomes public:

1. Revoke/rotate it.
2. Generate a new credential.
3. Update your deployment Config Vars.
4. Restart the bot.

---

# 🐛 Troubleshooting

## Assistant isn't joining VC

Check:

```text
✓ STRING_SESSION is valid
✓ Assistant is a member of the group
✓ Assistant has required permissions
✓ Voice chat is started
✓ API_ID is correct
✓ API_HASH is correct
✓ Voice-chat dependencies are installed
✓ FFmpeg is installed
```

---

## Bot isn't responding

Check:

```text
✓ BOT_TOKEN
✓ API_ID
✓ API_HASH
✓ OWNER_ID
✓ Bot is running
✓ Bot has required permissions
```

---

## Music isn't playing

Check:

```text
✓ Assistant is online
✓ Assistant joined the group
✓ Voice chat is active
✓ FFmpeg is installed
✓ yt-dlp is working
✓ Network connection is available
```

---

# 📊 Project Monitoring

Repomusic provides runtime monitoring capabilities including:

```text
CPU Usage       █████████░ 90%
RAM Usage       ███████░░░ 70%
Internet        █████████░ 90%
Playback        ██████████ 100%
```

Actual values depend on your hosting environment.

---

# 🔄 Updates

To update your local installation:

```bash
cd Repomusic
git pull origin main
pip3 install -r requirements.txt
bash start
```

Always review changes before updating a production deployment.

---

# 🤝 Contributing

Contributions are welcome.

```bash
git clone https://github.com/dgravanbhaii/Repomusic.git
cd Repomusic

git checkout -b feature/my-feature

# Make your changes

git add .
git commit -m "Add: my feature"

git push origin feature/my-feature
```

Then open a Pull Request.

---

# ⭐ Support Repomusic

If you like this project:

### ⭐ Star the repository

[![Star Repomusic](https://img.shields.io/github/stars/dgravanbhaii/Repomusic?style=for-the-badge\&logo=github\&label=STAR%20REPOSITORY\&color=gold)](https://github.com/dgravanbhaii/Repomusic)

### 🍴 Fork the project

[![Fork Repomusic](https://img.shields.io/github/forks/dgravanbhaii/Repomusic?style=for-the-badge\&logo=github\&label=FORK)](https://github.com/dgravanbhaii/Repomusic/fork)

### 🐛 Report a bug

[![Issues](https://img.shields.io/github/issues/dgravanbhaii/Repomusic?style=for-the-badge\&logo=github)](https://github.com/dgravanbhaii/Repomusic/issues)

---

# 👑 Developer

<div align="center">

## 【DG】 RAVAN

### `@dgravanbhaii`

Telegram Bot Developer • Automation • Open Source

<br>

<a href="https://github.com/dgravanbhaii">
<img src="https://img.shields.io/badge/GitHub-dgravanbhaii-181717?style=for-the-badge&logo=github">
</a>

<a href="https://github.com/dgravanbhaii/Repomusic">
<img src="https://img.shields.io/badge/Repomusic-Repository-8A2BE2?style=for-the-badge&logo=github">
</a>

</div>

---

<div align="center">

### 👑 Developer

<a href="https://github.com/dgravanbhaii">
  <img src="https://img.shields.io/badge/GitHub-dgravanbhaii-181717?style=for-the-badge&logo=github">
</a>

<a href="https://t.me/YOUR_USERNAME">
  <img src="https://img.shields.io/badge/Telegram-Contact%20Me-26A5E4?style=for-the-badge&logo=telegram&logoColor=white">
</a>

<br><br>

### ⭐ Support Repomusic

<a href="https://github.com/dgravanbhaii/Repomusic">
  <img src="https://img.shields.io/github/stars/dgravanbhaii/Repomusic?style=for-the-badge&logo=github&label=⭐%20STAR%20REPOSITORY&color=gold">
</a>

<a href="https://github.com/dgravanbhaii/Repomusic/fork">
  <img src="https://img.shields.io/github/forks/dgravanbhaii/Repomusic?style=for-the-badge&logo=github&label=🍴%20FORK%20REPOSITORY">
</a>

</div>

# ❤️ Credits

Repomusic is built using open-source technologies and the Telegram ecosystem.

Credits and attribution for the underlying project/components are retained according to the repository's `LICENSE` and source files.

Special thanks to:

* Telegram
* Pyrogram ecosystem
* Voice-chat libraries
* yt-dlp
* FFmpeg
* Spotify ecosystem
* Python open-source community
* Original project contributors

---

# 📈 Roadmap

```text
🎵 Advanced Music System
        │
        ├── 🔄 Improved Queue
        ├── 🎧 Better Streaming
        ├── 📋 Playlist Management
        ├── 🎤 Assistant Improvements
        ├── 📊 Advanced Statistics
        ├── ⚡ Performance Improvements
        ├── 🛠️ Better Error Handling
        └── 🎨 Enhanced UI
```

---

<div align="center">

# 🎵 REPOMUSIC

### Stream • Play • Enjoy

<br>

**Built with ❤️ by `dgravanbhaii`**

<br>

<a href="https://github.com/dgravanbhaii/Repomusic">
<img src="https://img.shields.io/github/stars/dgravanbhaii/Repomusic?style=social">
</a>

<br><br>

⭐ **Star the repository if you like Repomusic!** ⭐

</div>
