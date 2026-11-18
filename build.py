"""
E-Learning Platform Fast Section Compiler
Concatenates modular section HTML files in ./sections/ into index.html and index_elaeltd_redesign.html.
Runs in ~0.02 seconds with zero external dependencies.
"""

import os
import sys
import time

SECTIONS_DIR = 'sections'
OUTPUT_FILES = ['index.html', 'index_elaeltd_redesign.html']

def build():
    start_time = time.time()
    
    if not os.path.isdir(SECTIONS_DIR):
        print(f"Error: Directory '{SECTIONS_DIR}' not found!")
        sys.exit(1)
        
    section_files = sorted([f for f in os.listdir(SECTIONS_DIR) if f.endswith('.html')])
    if not section_files:
        print(f"Error: No HTML files found in '{SECTIONS_DIR}'!")
        sys.exit(1)
        
    compiled_parts = []
    for sf in section_files:
        fpath = os.path.join(SECTIONS_DIR, sf)
        with open(fpath, 'r', encoding='utf-8') as f:
            compiled_parts.append(f.read())
            
    full_html = "".join(compiled_parts)
    
    for out_name in OUTPUT_FILES:
        with open(out_name, 'w', encoding='utf-8') as out_f:
            out_f.write(full_html)
            
    # Also sync into e-learning-platform/ if it exists
    standalone_dir = 'e-learning-platform'
    if os.path.isdir(standalone_dir):
        with open(os.path.join(standalone_dir, 'index.html'), 'w', encoding='utf-8') as out_f:
            out_f.write(full_html)
            
    elapsed = (time.time() - start_time) * 1000
    print(f"Build successful in {elapsed:.1f}ms! Compiled {len(section_files)} sections ({len(full_html):,} bytes) into {', '.join(OUTPUT_FILES)}.")

if __name__ == '__main__':
    build()
