<div align="center">

# 🎵 REPOMUSIC

### ⚡ Powerful • Fast • Reliable Telegram Music Bot

[![GitHub Stars](https://img.shields.io/github/stars/dgravanbhaii/Repomusic?style=for-the-badge\&logo=github\&color=gold)](https://github.com/dgravanbhaii/Repomusic/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/dgravanbhaii/Repomusic?style=for-the-badge\&logo=github)](https://github.com/dgravanbhaii/Repomusic/network/members)
[![GitHub Issues](https://img.shields.io/github/issues/dgravanbhaii/Repomusic?style=for-the-badge\&logo=github)](https://github.com/dgravanbhaii/Repomusic/issues)
[![License](https://img.shields.io/github/license/dgravanbhaii/Repomusic?style=for-the-badge)](https://github.com/dgravanbhaii/Repomusic/blob/main/LICENSE)

<br>

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=24&pause=1000&color=FF4D8D&center=true&vCenter=true&width=700&lines=Welcome+to+Repomusic+%F0%9F%8E%B5;Telegram+Voice+Chat+Music+Bot+%F0%9F%8E%A7;Stream+Music+Directly+Into+Voice+Chats+%E2%9A%A1;Built+for+Speed%2C+Stability+%26+Performance+%F0%9F%9A%80" alt="Repomusic Typing Animation">

<br>

**Repomusic** is a feature-rich Telegram music bot designed to stream audio and video directly into Telegram voice chats with a fast, interactive and administrator-friendly experience.

<br>

[🎵 Features](#-features) •
[⚙️ Configuration](#%EF%B8%8F-configuration) •
[🚀 Deployment](#-deployment) •
[🎛️ Commands](#%EF%B8%8F-commands) •
[🛠️ Development](#%EF%B8%8F-development)

</div>

---

## 🌟 About Repomusic

**Repomusic** is a Telegram music streaming bot built around Python, Pyrogram/Kurigram-based Telegram clients and Telegram voice-chat calling libraries.

It is designed to provide a complete music experience inside Telegram groups and channels, including:

* 🎧 Voice-chat music streaming
* 🔎 YouTube and online music search
* 📥 Audio/video downloading and processing
* 📋 Queue management
* ⏯️ Playback controls
* 🎵 Playlist support
* 🎤 Channel playback support
* 🤖 Assistant-based voice-chat streaming
* 📊 Bot statistics and system monitoring
* ⚡ Fast asynchronous processing
* 🔐 Owner and administrator controls
* ☁️ Heroku/VPS deployment support

The repository contains deployment files such as `Dockerfile`, `Procfile`, `heroku.yml`, `app.json`, `runtime.txt`, `setup`, and `start`, making the project suitable for multiple hosting workflows.

---

# ✨ Features

<table>
<tr>
<td width="50%">

### 🎵 Music System

* ▶️ Play songs directly in voice chats
* 🔎 Search music online
* 🎧 Audio streaming
* 🎬 Video playback
* 📋 Queue management
* ⏭️ Skip tracks
* ⏹️ Stop playback
* ⏸️ Pause / Resume
* 🔀 Queue-based playback

</td>
<td width="50%">

### ⚡ Performance

* 🚀 Asynchronous architecture
* ⚡ Fast response handling
* 📡 Real-time voice-chat streaming
* 🧠 Runtime queue management
* 📊 CPU/RAM monitoring
* 🌐 Internet speed monitoring
* 🧹 Automatic cleanup options
* 🔄 Restart/reboot support

</td>
</tr>

<tr>
<td width="50%">

### 🎛️ Playback Controls

* `/play`
* `/vplay`
* `/cplay`
* `/playforce`
* `/pause`
* `/resume`
* `/skip`
* `/seek`
* `/seekback`
* `/stop`
* `/end`

</td>
<td width="50%">

### 🤖 Smart Features

* 🎯 Auto suggestions
* 🧹 Auto-cleaning
* 📊 Chat statistics
* 👤 User statistics
* 📝 Logging
* 🎤 Assistant accounts
* 📡 Channel support
* 🔧 Remote configuration
* 🔄 Git/upstream update support

</td>
</tr>
</table>

---

# 🎧 How Repomusic Works

```text
              ┌─────────────────────┐
              │      Telegram       │
              │       User          │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │    Repomusic Bot    │
              │   Command Handler   │
              └──────────┬──────────┘
                         │
             ┌───────────┴───────────┐
             │                       │
             ▼                       ▼
      ┌──────────────┐       ┌──────────────┐
      │ Music Search │       │    Queue     │
      │  / Download  │       │   Manager    │
      └──────┬───────┘       └──────┬───────┘
             │                      │
             └──────────┬───────────┘
                        ▼
              ┌─────────────────────┐
              │   Voice Chat Layer  │
              │   Assistant Client  │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Telegram Voice Chat │
              │       🎵 🔊         │
              └─────────────────────┘
```

The bot handles commands and playback logic, while the Telegram assistant/client is used for voice-chat interaction and streaming.

---

# 🎛️ Commands

## 🎵 Music Commands

| Command       | Description                               |
| ------------- | ----------------------------------------- |
| `/play`       | Play a song in the current voice chat     |
| `/vplay`      | Play video/audio content                  |
| `/cplay`      | Play through channel mode                 |
| `/playforce`  | Force play and replace the current stream |
| `/vplayforce` | Force video playback                      |
| `/cplayforce` | Force channel playback                    |
| `/skip`       | Skip the currently playing track          |
| `/pause`      | Pause the current stream                  |
| `/resume`     | Resume the paused stream                  |
| `/stop`       | Stop playback and clear the queue         |
| `/end`        | End the current playback session          |
| `/seek`       | Seek forward to a specified duration      |
| `/seekback`   | Seek backward to a specified duration     |

---

## 📡 Channel Playback

Repomusic supports channel-based playback.

Use:

```text
/channelplay <channel_username_or_id>
```

To disable channel playback:

```text
/channelplay disable
```

The bot and assistant should have the required administrator permissions in the relevant channel/group setup.

---

# ⚙️ Configuration

Repomusic uses environment variables for configuration.

Create your environment file using the repository's `sample.env` as the reference.

### Required Core Variables

```env
API_ID=
API_HASH=
BOT_TOKEN=
LOGGER_ID=
OWNER_ID=
STRING_SESSION=
```

### Database

```env
MONGO_DB_URI=
```

The current configuration supports a MongoDB URI. Configure it according to the database features enabled in your deployment.

### Optional Configuration

```env
COOKIES=

DURATION_LIMIT=
SONG_DOWNLOAD_DURATION_LIMIT=

BOT_USERNAME=
COMMAND_HANDLER=

HEROKU_APP_NAME=
HEROKU_API_KEY=

UPSTREAM_REPO=
UPSTREAM_BRANCH=
GIT_TOKEN=

SUPPORT_CHANNEL=
SUPPORT_CHAT=

AUTO_LEAVING_ASSISTANT=
AUTO_SUGGESTION_MODE=
AUTO_SUGGESTION_TIME=

SPOTIFY_CLIENT_ID=
SPOTIFY_CLIENT_SECRET=

PLAYLIST_FETCH_LIMIT=
CLEANMODE_MINS=

TG_AUDIO_FILESIZE_LIMIT=
TG_VIDEO_FILESIZE_LIMIT=
```

### Multiple Assistant Sessions

Repomusic supports multiple string-session configuration slots:

```env
STRING_SESSION=
STRING_SESSION2=
STRING_SESSION3=
STRING_SESSION4=
STRING_SESSION5=
```

Use only the sessions you actually need.

---

# 🔑 Environment Variables Explained

| Variable                | Purpose                           |
| ----------------------- | --------------------------------- |
| `API_ID`                | Telegram API ID                   |
| `API_HASH`              | Telegram API hash                 |
| `BOT_TOKEN`             | Telegram bot token                |
| `OWNER_ID`              | Bot owner's Telegram user ID      |
| `LOGGER_ID`             | Logging chat/channel ID           |
| `STRING_SESSION`        | Assistant Telegram session        |
| `STRING_SESSION2`       | Optional second assistant         |
| `STRING_SESSION3`       | Optional third assistant          |
| `STRING_SESSION4`       | Optional fourth assistant         |
| `STRING_SESSION5`       | Optional fifth assistant          |
| `MONGO_DB_URI`          | MongoDB connection URI            |
| `COOKIES`               | Optional media extraction cookies |
| `BOT_USERNAME`          | Bot username                      |
| `COMMAND_HANDLER`       | Command prefixes                  |
| `SUPPORT_CHANNEL`       | Support/update channel            |
| `SUPPORT_CHAT`          | Support group                     |
| `SPOTIFY_CLIENT_ID`     | Spotify API client ID             |
| `SPOTIFY_CLIENT_SECRET` | Spotify API client secret         |
| `UPSTREAM_REPO`         | Upstream Git repository           |
| `UPSTREAM_BRANCH`       | Git branch                        |
| `AUTO_SUGGESTION_MODE`  | Automatic suggestion mode         |
| `AUTO_SUGGESTION_TIME`  | Suggestion timing                 |
| `PLAYLIST_FETCH_LIMIT`  | Playlist fetching limit           |
| `CLEANMODE_MINS`        | Automatic cleanup interval        |

---

# 🧰 Requirements

The project uses a Python-based asynchronous stack with packages including:

* 🐍 Python
* 📱 Pyrogram/Kurigram
* 🎙️ Py-TGCALLS / NTGCALLS
* 🎵 yt-dlp
* 🎧 FFmpeg
* 🎼 Spotipy
* 🗄️ Motor / MongoDB support
* 🌐 aiohttp
* ⚡ uvloop
* 🖼️ Pillow
* 📊 psutil
* 🔧 GitPython
* ☁️ Heroku tooling

The exact dependencies are maintained in [`requirements.txt`](./requirements.txt).

---

# 🚀 Deployment

## ☁️ Heroku

Repomusic includes Heroku deployment configuration.

### 1. Fork the repository

Fork:

```text
https://github.com/dgravanbhaii/Repomusic
```

### 2. Create a Heroku application

Create a new Heroku app and connect your repository.

### 3. Configure environment variables

Open:

```text
Heroku Dashboard
       ↓
Your App
       ↓
Settings
       ↓
Config Vars
```

Add the required environment variables.

At minimum:

```env
API_ID
API_HASH
BOT_TOKEN
OWNER_ID
LOGGER_ID
STRING_SESSION
```

Add the database and optional variables required by your setup.

### 4. Deploy

Deploy the `main` branch.

The repository already includes:

```text
Procfile
heroku.yml
app.json
runtime.txt
```

for deployment support.

---

# 🖥️ VPS / Local Deployment

## 1. Install system dependencies

Ubuntu/Debian:

```bash
sudo apt update
sudo apt install -y python3 python3-pip ffmpeg git
```

## 2. Clone the repository

```bash
git clone https://github.com/dgravanbhaii/Repomusic.git
cd Repomusic
```

## 3. Install Python dependencies

```bash
pip3 install -r requirements.txt
```

## 4. Configure environment variables

Create your environment configuration:

```bash
cp sample.env .env
```

Then edit:

```bash
nano .env
```

Add your Telegram credentials, bot token, owner ID, logger ID, assistant session and other required values.

## 5. Run setup

```bash
bash setup
```

## 6. Start Repomusic

```bash
bash start
```

---

# 🐳 Docker

Repomusic also contains a `Dockerfile`.

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

Check logs:

```bash
docker logs -f repomusic
```

---

# 🔐 Telegram Permissions

For reliable voice-chat playback, make sure the bot/assistant accounts have the required permissions.

### Group

Recommended permissions:

```text
✓ Manage Video Chats
✓ Invite Users
✓ Send Messages
✓ Delete Messages
```

### Channel

When using channel playback, add the bot and assistant as administrators with the permissions required by your configuration.

---

# 🎤 Assistant Account

Telegram bots cannot independently behave like a normal Telegram user account inside every voice-chat workflow.

Repomusic therefore supports a Telegram assistant session through:

```env
STRING_SESSION=
```

Additional assistant sessions can be configured with:

```env
STRING_SESSION2=
STRING_SESSION3=
STRING_SESSION4=
STRING_SESSION5=
```

### Important

Never publish your:

```text
BOT_TOKEN
API_HASH
STRING_SESSION
MONGO_DB_URI
HEROKU_API_KEY
SPOTIFY_CLIENT_SECRET
```

in GitHub, screenshots, logs or public channels.

If a secret is exposed, rotate it immediately.

---

# 📊 Monitoring

Repomusic includes runtime-oriented configuration for statistics and monitoring.

Depending on the enabled modules, the project can track:

```text
CPU usage
RAM usage
Network usage
Chat statistics
User statistics
Playback state
Queue state
```

This makes it easier to monitor the bot during VPS or cloud deployment.

---

# 🔄 Upstream / Git Integration

The configuration includes support for an upstream repository:

```env
UPSTREAM_REPO=https://github.com/dgravanbhaii/Repomusic
UPSTREAM_BRANCH=main
```

For private repositories, a Git token can be supplied through:

```env
GIT_TOKEN=
```

Keep private repository tokens out of your source code.

---

# 🧹 Auto Features

Repomusic provides configurable automation options.

### Auto Suggestions

```env
AUTO_SUGGESTION_MODE=True
AUTO_SUGGESTION_TIME=500
```

### Assistant Auto Leaving

```env
AUTO_LEAVING_ASSISTANT=
```

### Automatic Cleanup

```env
CLEANMODE_MINS=5
```

These values can be adjusted according to your deployment requirements.

---

# 🎨 Customization

Several UI image URLs can be customized from the configuration.

Examples include:

```env
START_IMG_URL=
PING_IMG_URL=
```

The configuration also supports separate image resources for music/search-related interfaces.

This allows you to create your own branded Repomusic experience without changing the core playback engine.

---

# 📁 Repository Structure

```text
Repomusic/
│
├── 📂 ShashankMusic/       # Main bot/music source modules
├── 📂 strings/             # Bot strings and messages
│
├── 🐍 config.py            # Main configuration
├── 📦 requirements.txt     # Python dependencies
├── ⚙️ sample.env           # Environment template
│
├── 🚀 start                # Startup script
├── 🔧 setup                # Setup script
│
├── 🐳 Dockerfile           # Docker configuration
├── ☁️ Procfile             # Process definition
├── ☁️ heroku.yml           # Heroku deployment configuration
├── 📱 app.json             # Application metadata
├── 🐍 runtime.txt          # Runtime specification
│
├── 📜 LICENSE              # Project license
└── 📖 README.md            # Documentation
```

---

# 🛠️ Development

Clone the project:

```bash
git clone https://github.com/dgravanbhaii/Repomusic.git
cd Repomusic
```

Create an isolated environment:

```bash
python3 -m venv venv
```

Activate it on Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure:

```bash
cp sample.env .env
```

Then start the bot:

```bash
bash start
```

---

# 🧩 Troubleshooting

### ❌ Assistant is not joining the voice chat

Check:

```text
✓ STRING_SESSION is valid
✓ Assistant account is active
✓ Assistant is a member of the group
✓ Assistant has required permissions
✓ Voice chat is actually started
✓ API_ID and API_HASH are correct
✓ Py-TGCALLS/NTGCALLS dependencies installed
✓ FFmpeg is installed
```

---

### ❌ Bot starts but commands do not work

Check:

```text
✓ BOT_TOKEN
✓ API_ID
✓ API_HASH
✓ OWNER_ID
✓ BOT_USERNAME
✓ COMMAND_HANDLER
```

Also verify that the bot is actually running and that Telegram can reach the deployment.

---

### ❌ Music extraction fails

Check:

```text
✓ yt-dlp is installed
✓ FFmpeg is installed
✓ Network connectivity
✓ COOKIES configuration if required
✓ Media source availability
```

---

### ❌ Heroku deployment fails

Check:

```text
✓ requirements.txt
✓ runtime.txt
✓ Config Vars
✓ Procfile
✓ heroku.yml
✓ Build logs
✓ Required environment variables
```

---

# 📜 License

This project includes a `LICENSE` file in the repository.

Before redistributing, modifying or deploying a derivative version, review the actual license terms contained in:

```text
LICENSE
```

Do not remove required attribution or license notices from source files where applicable.

---

# 🤝 Contributing

Contributions are welcome.

### Contribution workflow

```bash
# Fork the repository

# Clone your fork
git clone https://github.com/YOUR_USERNAME/Repomusic.git

# Create a branch
git checkout -b feature/my-feature

# Make your changes

# Commit
git add .
git commit -m "Add: my feature"

# Push
git push origin feature/my-feature
```

Then open a Pull Request.

### Good contribution areas

```text
🎵 Playback improvements
⚡ Performance optimization
🐛 Bug fixes
🎨 UI improvements
🔧 Deployment improvements
📚 Documentation
🔐 Security improvements
🧪 Testing
```

---

# 💬 Support

Need help with Repomusic?

### 📢 Support Channel

[Join the Support Channel](https://t.me/Il_Ravan_bhai_ll)

### 💬 Support Group

[Join the Support Group](https://t.me/+y9SXssXwKsIzMGRl)

---

# ⭐ Support the Project

If Repomusic is useful to you:

### ⭐ Star the repository

A GitHub star helps the project gain visibility.

### 🍴 Fork it

Create your own version and improve it.

### 🐛 Report issues

Found a bug?

Open a GitHub Issue with:

```text
Environment:
Python version:
Hosting:
Error:
Logs:
Steps to reproduce:
```

---

# 🧑‍💻 Developer

<div align="center">

### 👑 RAVAN

**Developer & Maintainer**

Building Telegram automation, music bots and developer tools.

<br>

[![GitHub](https://img.shields.io/badge/GitHub-dgravanbhaii-black?style=for-the-badge\&logo=github)](https://github.com/dgravanbhaii)

[![Repomusic](https://img.shields.io/badge/Repository-Repomusic-purple?style=for-the-badge\&logo=github)](https://github.com/dgravanbhaii/Repomusic)

</div>

---

# ❤️ Credits

Repomusic is built using a combination of open-source technologies and Telegram ecosystem tools.

Special thanks to the developers and maintainers of:

* Telegram
* Pyrogram / Kurigram ecosystem
* Py-TGCALLS / NTGCALLS
* yt-dlp
* FFmpeg
* Spotipy
* Python open-source ecosystem

Respect the original licenses and attribution requirements of all dependencies.

---

# 📈 Project Status

```text
┌─────────────────────────────────────────┐
│              REPOMUSIC                  │
├─────────────────────────────────────────┤
│ 🎵 Music Streaming       ██████████ 100%│
│ 🎧 Voice Chat            ██████████ 100%│
│ 📋 Queue System          ██████████ 100%│
│ ⚡ Async Processing      ██████████ 100%│
│ ☁️ Cloud Deployment      ██████████ 100%│
│ 🐳 Docker Support        ██████████ 100%│
│ 🔧 Customization         ██████████ 100%│
└─────────────────────────────────────────┘
```

> Status represents the project's documented capabilities and configuration, not a guarantee that every deployment configuration will work without environment-specific setup.

---

# 🚀 Repomusic Roadmap

Future improvements can include:

```text
[ ] Advanced playlist management
[ ] Better queue controls
[ ] Improved search engine integration
[ ] More streaming sources
[ ] Enhanced admin controls
[ ] Improved statistics dashboard
[ ] More assistant automation
[ ] Better error recovery
[ ] Performance optimization
[ ] Expanded deployment options
```

---

<div align="center">

## 🎵 REPOMUSIC

### Stream. Play. Enjoy. 🚀

**Made with ❤️ for the Telegram music community**

<br>

⭐ **If you like Repomusic, don't forget to star the repository!** ⭐

<br>

[![Star Repo](https://img.shields.io/github/stars/dgravanbhaii/Repomusic?style=social)](https://github.com/dgravanbhaii/Repomusic)

</div>
