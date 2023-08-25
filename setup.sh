mkdir -p ~/.streamlit/

echo "\
[server]\n\
port=$PORT\n\
enableCORS=false\n\
headless=true\n\
\n\
" > ~/.streamlit/confi.toml
web: sh setup.sh &&streamlit run app.py