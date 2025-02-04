# 📊 ChatGPT Heatmap Generator

ChatGPT Heatmap Generator is a Python tool that visualizes ChatGPT conversation activity over a year using a **heatmap**. It loads conversation timestamps from a JSON file and plots a color-coded heatmap to highlight the most active days.

---

## 🚀 Features

✅ **Visualize Activity Trends** – Get insights into ChatGPT conversation frequency over the year.\
✅ **Timezone Support** – Automatically converts timestamps to a given timezone.\
✅ **Customizable Heatmap** – Adjust colors and thresholds for better clarity.\
✅ **Easy to Use** – Just provide a JSON file and run the script.\
✅ **Matplotlib-Based** – Uses Python's powerful visualization library.


---

## 🖼️ Screenshots

![Screenshot](https://github.com/IAnuragMahapatra/chatgpt-heatmap/blob/36d4e893369ec7bb3396cd89c2cfe7d562e53e7f/Screenshots/Screenshot1.png)


---

## 🛠 Installation & Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/IAnuragMahapatra/chatgpt-heatmap.git
cd chatgpt-heatmap
```

### 2️⃣ Install Dependencies

Install the required Python packages using:

```bash
pip install matplotlib numpy pytz
```

### 3️⃣ Prepare Your Data

- **Export ChatGPT Conversations**:
  - Go to [ChatGPT](https://chatgpt.com/) and sign in to your account.
  - Go to **Settings > Data Controls > Export Data** in ChatGPT.
  - You will receive an email with a download link.
  - Download and extract the exported data.
  - Copy `conversations.json` to the script directory.
- Ensure your JSON file contains conversation timestamps in UNIX format.

### 4️⃣ Run the Script

```bash
python script.py
```

---

## 📑 JSON File Format (`conversations.json`)

The script expects a JSON file containing a list of ChatGPT conversations with timestamps. Example:

```json
[
  {"create_time": 1704067200},
  {"create_time": 1704153600},
  {"create_time": 1704240000}
]
```

Each conversation entry must have a `create_time` field with a **UNIX timestamp** (seconds since epoch).

---

## ⚙️ Configuration

Modify the following parameters in `heatmap.py`:

- **Timezone**: Change `tz_name` to your preferred timezone.
- **Year**: Update the year in `generate_heatmap()` to visualize a specific year.
- **Color Scheme**: Adjust `plt.cm.Greens` for a different heatmap color.

### 🎨 Changing the Heatmap Color

Replace `plt.cm.Greens` with another Matplotlib colormap like:

- `plt.cm.Blues` (blue shades)
- `plt.cm.Reds` (red shades)
- `plt.cm.Oranges` (orange shades)
- `plt.cm.Purples` (purple shades)
- `plt.cm.coolwarm` (cool-warm contrast)
- `plt.cm.viridis` (visually uniform)

Example:

```python
color = plt.cm.Blues(min((count / p90_value), 1)) if count > 0 else 'lightgray'
```

---

## 💍 Credits & License

This project is **open-source** under the **MIT License**. Contributions are welcome!

---

## 💌 Contact

👤 **Author**: Anurag Mahapatra\
📧 **Email**: [anurag2005om@gmail.com](mailto:anurag2005om@gmail.com)\
🌐 **GitHub**: [IAnuragMahapatra](https://github.com/IAnuragMahapatra)

See your ChatGPT conversations in a whole new way! 🔥📊

