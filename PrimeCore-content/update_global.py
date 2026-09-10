import os
from bs4 import BeautifulSoup

def update_html_file(filepath):
    with open(filepath, 'r') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    
    # Calculate depth
    rel_path = os.path.relpath(filepath, '.')
    depth = rel_path.count(os.sep)
    prefix = '../' * depth if depth > 0 else './'

    # Update body class
    if soup.body:
        # Add reference-home to all body tags to get the unified look
        classes = soup.body.get('class', [])
        if 'reference-home' not in classes:
            classes.append('reference-home')
        soup.body['class'] = classes

    # 1. Update CSS Links
    if soup.head:
        # Remove existing custom CSS links
        for link in soup.head.find_all('link', rel='stylesheet'):
            if 'css' in link.get('href', ''):
                link.decompose()
        
        # Add uniform CSS
        css_files = [
            'assets/css/reference-home.css',
            'assets/css/cloud-asset.css',
            'assets/css/site-pages.css',
            'assets/css/glass-panels.css',
            'assets/css/heading-style.css'
        ]
        for css in css_files:
            new_link = soup.new_tag('link', rel='stylesheet', href=prefix + css)
            soup.head.append(new_link)
            soup.head.append('\n')

    # 2. Update Header
    header_html = f'''
    <header class="reference-header" id="global-header">
      <a class="reference-brand" href="{prefix}" aria-label="Primecoreinfo home">
        <span class="brand-diamond"></span><span>PRIMECOREINFO</span>
      </a>
      <nav class="reference-nav" aria-label="Primary navigation">
        <a href="{prefix}about/">About</a>
        <a href="{prefix}services/">Services</a>
        <a href="{prefix}insights/">Insights</a>
        <a href="{prefix}contact/">Contact</a>
        <a class="reference-login" href="{prefix}contact/">Let's talk</a>
      </nav>
      <button class="reference-menu" type="button" aria-expanded="false" aria-controls="reference-mobile-menu">
        <span></span><span></span><span></span><b class="sr-only">Open menu</b>
      </button>
    </header>
    
    <nav class="reference-mobile-menu" id="reference-mobile-menu" hidden aria-label="Mobile navigation">
      <a href="{prefix}about/">About</a>
      <a href="{prefix}services/">Services</a>
      <a href="{prefix}insights/">Insights</a>
      <a href="{prefix}contact/">Contact</a>
    </nav>
    '''
    
    new_header = BeautifulSoup(header_html, 'html.parser')
    
    # Remove old header
    old_header = soup.find('header')
    old_mobile_nav = soup.find('nav', id='reference-mobile-menu')
    if old_header:
        old_header.insert_before(new_header)
        old_header.decompose()
        if old_mobile_nav:
            old_mobile_nav.decompose()
    elif soup.body:
        soup.body.insert(0, new_header)

    # 3. Add Sky Glows if missing
    if soup.body and not soup.find(class_='sky-glow'):
        sky_glows = BeautifulSoup('<div class="sky-glow sky-glow-one"></div><div class="sky-glow sky-glow-two"></div>', 'html.parser')
        soup.body.insert(0, sky_glows)

    # 4. Update Footer
    footer_html = f'''
    <footer class="reference-footer">
      <span>PRIMECOREINFO / IT CLOUD TRANSFORMATION</span>
      <a href="{prefix}privacy-policy/">Privacy</a>
      <a href="{prefix}insights/">Insights</a>
      <a href="mailto:hello@primecoreinfo.com">Email</a>
    </footer>
    '''
    new_footer = BeautifulSoup(footer_html, 'html.parser')
    
    old_footer = soup.find('footer')
    if old_footer:
        old_footer.insert_before(new_footer)
        old_footer.decompose()
    elif soup.body:
        soup.body.append(new_footer)

    # 5. Ensure JS is linked
    if soup.body and not soup.find('script', src=lambda s: s and 'reference-home.js' in s):
        new_script = soup.new_tag('script', src=prefix + 'assets/js/reference-home.js')
        soup.body.append(new_script)

    with open(filepath, 'w') as f:
        f.write(str(soup))

if __name__ == '__main__':
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                update_html_file(os.path.join(root, file))
    print("Done updating HTML files.")
