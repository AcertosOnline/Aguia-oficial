from datetime import datetime

# Gera o sitemap com a data atual
current_date = datetime.now().strftime('%Y-%m-%d')

sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://aguia-oficial.com/</loc>
        <lastmod>{current_date}</lastmod>
        <changefreq>daily</changefreq>
        <priority>1.0</priority>
    </url>
</urlset>
"""

# Salva o conteúdo no arquivo sitemap.xml
with open("sitemap.xml", "w") as file:
    file.write(sitemap_content)

print("Sitemap gerado com sucesso!")
