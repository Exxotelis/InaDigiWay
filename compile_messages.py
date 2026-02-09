#!/usr/bin/env python
"""
Compile .po files to .mo files without requiring GNU gettext tools.
This script uses the polib library.
"""

import os
import sys

def compile_po_to_mo():
    """Compile all .po files to .mo files"""
    try:
        import polib
    except ImportError:
        print("Installing polib...")
        os.system(f"{sys.executable} -m pip install polib")
        import polib
    
    # Find all .po files
    locale_dir = 'locale'
    for root, dirs, files in os.walk(locale_dir):
        for file in files:
            if file.endswith('.po'):
                po_path = os.path.join(root, file)
                mo_path = po_path.replace('.po', '.mo')
                
                print(f"Compiling {po_path} -> {mo_path}")
                
                try:
                    # Load the .po file
                    po = polib.pofile(po_path)
                    
                    # Save as .mo file
                    po.save_as_mofile(mo_path)
                    print(f"✓ Successfully compiled {mo_path}")
                except Exception as e:
                    print(f"✗ Error compiling {po_path}: {e}")
    
    print("\n✓ All .po files compiled to .mo!")

if __name__ == '__main__':
    compile_po_to_mo()
