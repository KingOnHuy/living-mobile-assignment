# Group Name : Sinopharm
## Members
1. Ponpawit Paoseng (King)
2. Chukeit Panpiboon (Arm)

## Backoffice Assignment
- Store: Arm (UI,Vuex)
- Category: Arm(UI), King(Vuex)
- Menu: King (UI,Vuex)
# เกณท์ในการแบ่งงาน
1. Arm เรื่มทำจากหน้า Store ไล่ไปเรื่อยๆ
2. King เริ่มทำ Authentication และจึงเริ่มทำจากหน้าสุดท้ายย้อนหลังมาเรื่อยๆ
3. King ทำ Vuex `category` module ที่จำเป็นต้องใช้สำหรับหน้า Store
# Getting Started
This project uses the Django Rest framework (DRF) as a backend.

Ponpawit Paoseng
## Prerequisites

0. Use Linux OS
1. Install Docker [read more](https://docs.docker.com/engine/install/ubuntu/)
    1. Install docker
        ```
        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
        ```
        ```
        echo \
        "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
        ```
        ```
        sudo apt-get update
        sudo apt-get install docker-ce docker-ce-cli containerd.io
        ```
    2. Post-installation steps for Linux [(read more)](https://docs.docker.com/engine/install/linux-postinstall/)
        ```
        sudo groupadd docker
        sudo usermod -aG docker $USER
        ```
    3. Log out and log back in so that your group membership is re-evaluated
2. Start Docker service
    ```
    sudo systemctl start docker
    ```
2. Install Docker compose [read more](https://docs.docker.com/compose/install/#install-compose-on-linux-systems)

    1. Run this command to download the current stable release of Docker Compose:
        ```
        sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
        ```
    2. Apply executable permissions to the binary:
        ```
        sudo chmod +x /usr/local/bin/docker-compose
        ```

## Installation Backend
1. Create docker network `livingmobile-networks`
    ```
    docker network create livingmobile-networks
    ```
2. Setup .env file
    1. Database `database/.env`
        ```
        POSTGRES_DB=< Database name >
        POSTGRES_USER=< Database user >
        POSTGRES_PASSWORD=< Database password >

        POSTGRES_HOST=postgres
        POSTGRES_PORT=5432
        ```
    2. Backend REST DRF `backend_rest_drf/.env`
        > Note.
        > The `production` state has not been handled yet.

        ```
        STATE=development

        SECRET_KEY=< Django Secret Key >

        POSTGRES_DB=< Database name >
        POSTGRES_USER=< Database user >
        POSTGRES_PASSWORD=< Database password >

        POSTGRES_HOST=postgres
        POSTGRES_PORT=5432
        ```
        > Note.
        >
        > If you have Python with `django` installed, You can generate django secret key with this command.
        >
        > `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
3. Start Database
    ```
    cd database
    docker-compose up -d
    ```
4. Start Backend REST DRF
    ```
    cd backend_rest_drf
    docker-compose up -d
    ```
    #### Create Super user
        ```
        docker-compose exec backend_rest_drf-web bash
        python manage.py createsuperuser
        ```
5. Open browser
    - Backend REST
      - Django Admin `http://localhost:8989/admin/`
      - Swagger `http://localhost:8989/swagger/`
      - ReDoc `http://localhost:8989/redoc/`
      - API Root `http://localhost:8989/v1/`
    - DBMS (pgAdmin)
      - `http://localhost:5050/`

## Installation Frontend
1. Install packages
    ```
    yarn
    ```
2. Run
   ```
   yarn serve
   ```
> Note. You must be `Create Super user` for login [(here)](#create-super-user)
## Test
1. Exec to `backend_rest_drf`
    ```
    docker-compose exec backend_rest_drf-web bash
    ```
2. Run test command
    ```
    python manage.py test
    ```