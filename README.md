**ReadMe: Setting Up Environment, Database, and Running the Server**

Dear STARNSLAUS KILUNDI,

Thank you for using our script. To complete the setup and run the server, please follow the steps outlined below:

### Setting Environment Variable

Before proceeding, ensure you have set the environment variable as mentioned earlier:

```powershell
$env:READ_DOT_ENV_FILE = "True"
```

### First-Time Database Creation

If this is your initial run, create a new database with the provided credentials:

- **Database Name:** crmdb
- **Database User:** muthi
- **Database Password:** kilundi

### Running Tailwind CSS

To start Tailwind CSS, use the following command:

```bash
python manage.py tailwind start
```

This command initiates the Tailwind CSS build process.

### Running the Server

Finally, to launch the server, execute:

```bash
python manage.py runserver
```

This command starts the development server, allowing you to access your application.

### Additional Information

For PostgreSQL database user creation, please refer to [this link](https://www.guru99.com/postgresql-create-alter-add-user.html).

Feel free to reach out if you encounter any issues during the setup or have further questions.

Best regards,

[StarTech]
