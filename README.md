# fullfeblog
echo "# fullfeblog" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:mrpal39/fullfeblog.git
git push -u origin main
pip install social-auth-app-django

pip install django-extensions
pip install werkzeug
pip install pyOpenSSL