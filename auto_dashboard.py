from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def extract_views_comments():
    # Configuração do driver do Selenium
    chrome_options = Options()
    chrome_options.headless = False  # Mudar para True se quiser rodar sem interface gráfica
    service = Service('chromedriver.exe')  
    
    # Inicializar o driver do Selenium
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # URL do vídeo do YouTube
    url = 'https://www.youtube.com/watch?v=HQ2VYbedE1g'  # Substitua pelo ID do vídeo

    # Abrir a página do vídeo
    driver.get(url)

    try:
        # Espera explícita para o elemento estar presente e visível
        views_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[4]/div[1]/div/ytd-watch-info-text/div/yt-formatted-string/span[1]'))
        )
    
        # Obter o texto das visualizações e comentários
        views = views_element.text
        print(f"O vídeo tem {views}.")

    except Exception as e:
        print(f"Erro ao encontrar o elemento: {e}")

    try:
        # Espera explícita para o elemento estar presente e visível
        comment_element = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-comments/ytd-item-section-renderer/div[1]/ytd-comments-header-renderer/div[1]/div[1]'))
        )
    
        # Obter o texto das visualizações e comentários
        comments = comment_element.text
        print(f"O vídeo tem {comments}.")

    except Exception as e:
        print(f"Erro ao encontrar o elemento: {e}")
        
    finally:
        # Fechar o navegador
        driver.quit()
