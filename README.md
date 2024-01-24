Amazon Returns Manager
This Django application allows users to manage dispute cases for Amazon returns, integrating order data.

Prerequisites
Python 3.10
Docker
Docker Compose

Clone the repository:
git clone https://github.com/yourusername/amazon_returns_manager.git
cd amazon_returns_manager

Create a virtual environment and activate it:
python -m venv amazon_returns_env
source amazon_returns_env/bin/activate # On Windows, use `amazon_returns_env\Scripts\activate`

Install project dependencies:
pip install -r requirements.txt

Build and run Docker containers:
docker-compose up --build

Visit below urls
disputes list: Visit http://127.0.0.1:8000/disputes/orders/ and follow the instructions. - you can manage update or delete disputes from above url
Create disputes: Visit http://127.0.0.1:8000/disputes/create/ and follow the instructions.

Technologies - Django - PostgreSQL - Docker
