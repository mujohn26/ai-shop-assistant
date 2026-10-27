# 🛍️ AI Shop Assistant

**A friendly AI-powered sales assistant for clothing stores — answers customer questions about products, prices, sizes and availability, 24/7.**

Small shops lose sales every day because no one is available to answer simple questions like *"Do you have this in size M?"* or *"What can I get under 20,000 RWF?"*. AI Shop Assistant solves that with a conversational chatbot that knows your entire catalog and responds instantly, in natural language.

Built with Python, Gradio and a large language model, it's lightweight, easy to customize, and can be adapted to any store in minutes — just edit a JSON file.

---

## ✨ Features

- **Natural conversations** — customers chat just like they would with a real shop assistant.
- **Knows your catalog** — answers questions about products, prices, colors, sizes and stock using your own product data.
- **Smart recommendations** — suggests items based on budget, style, occasion or category.
- **Honest about availability** — tells customers when an item is out of stock instead of making things up.
- **Remembers the conversation** — follow-up questions like *"Does it come in black?"* just work.
- **No-code updates** — change products or the assistant's personality by editing simple text and JSON files.
- **Clean web interface** — a ready-to-use chat UI powered by Gradio.

---

## 💬 Example conversation

> **Customer:** Hi! I'm looking for something to wear to a casual party, under 25,000 RWF.
>
> **Assistant:** Great choice! Here are a few options within your budget:
> - **Kitenge Print Shirt** – 22,000 RWF, available in Orange and Green (sizes M–XL)
> - **Hooded Sweatshirt** – 18,000 RWF, in Grey, Black or Maroon
> - **High-Waist Trousers** – 20,000 RWF, in Beige or Black
>
> Would you like help picking a size?
>
> **Customer:** Do you have the rain jacket?
>
> **Assistant:** Sorry, the Lightweight Rain Jacket is currently out of stock. The Hooded Sweatshirt could be a cozy alternative for cool evenings!

---

## 🧰 Tech stack

| Tool | Purpose |
|------|---------|
| [Python 3.12](https://www.python.org/) | Core language |
| [uv](https://docs.astral.sh/uv/) | Fast dependency & environment management |
| [Gradio](https://www.gradio.app/) | Chat web interface |
| LLM API | Powers the assistant's responses |
| python-dotenv | Secure API key loading |

---

## 📁 Project structure

```
ai-shop-assistant/
├── data/
│   └── products.json          # Store product catalog
├── prompts/
│   └── system.txt             # Assistant personality & store rules
├── src/
│   └── ai_shop_assistant/
│       ├── __init__.py
│       ├── app.py             # Gradio app entry point
│       └── chat_model.py      # LLM logic & message handling
├── .env                       # API key (not committed)
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## 🚀 Getting started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/ai-shop-assistant.git
cd ai-shop-assistant
```

### 2. Install dependencies

Make sure [uv](https://docs.astral.sh/uv/getting-started/installation/) is installed, then run:

```bash
uv sync
```

### 3. Add your API key

Create a `.env` file in the project root:

```env
API_KEY=your_api_key_here
```

### 4. Run the app

```bash
uv run ai-shop-assistant
```

Then open **http://127.0.0.1:7860** in your browser and start chatting. 🎉

---

## 🛠️ Customize it for your store

### Update your products

Edit `data/products.json`. Each product looks like this:

```json
{
  "id": "P004",
  "name": "Kitenge Print Shirt",
  "category": "Shirts",
  "gender": "Men",
  "price": 22000,
  "currency": "RWF",
  "sizes": ["M", "L", "XL"],
  "colors": ["Orange", "Green"],
  "in_stock": true,
  "description": "Short-sleeve shirt made from colorful African kitenge fabric."
}
```

Add, remove or edit items — the assistant picks up changes the next time the app starts.

### Change the assistant's personality

Edit `prompts/system.txt` to set the tone, store name, opening hours, delivery options, return policy, or anything else customers often ask about.

---

## 🗺️ Roadmap

- [ ] Product images in chat responses
- [ ] Size recommendations based on customer measurements
- [ ] Multilingual support (Kinyarwanda, French, English, Swahili)
- [ ] WhatsApp integration
- [ ] Order placement and stock updates via a database
- [ ] Admin dashboard for managing products

---

## 🤝 Contributing

Contributions, ideas and feedback are welcome! Feel free to open an issue or submit a pull request.

1. Fork the project
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m "Add amazing feature"`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a pull request

---

## 📄 License

This project is licensed under the MIT License.

---

<p align="center">Made with ❤️ to help small businesses sell smarter.</p>