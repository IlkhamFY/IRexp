# Cover letter: IRexp (Scientific Data)

**Manuscript:** IRexp: A database of experimental infrared band lists from open-access literature
**Article type:** Data Descriptor
**Journal:** Scientific Data
**Authors:** Ilkham Yabbarov; Rudra Sondhi; Rodrigo A. Vargas-Hernández
**Signatory:** Rodrigo A. Vargas-Hernández (vargashr@mcmaster.ca), on behalf of all authors
**Source:** `cover_letter.tex` (McMaster letterhead, `mcm-col_png.png`)

---

Dear Editor,

We submit our manuscript entitled *IRexp: A database of experimental infrared band lists from open-access literature* for consideration as a Data Descriptor in *Scientific Data*.
IRexp is a collection of experimental infrared band lists (cm⁻¹ peak positions) mined from PMC Open Access full text and supporting information and from a Chemotion repository deposit.
Of 239,735 harvested records, 230,946 are deposited, from 19,859 PMC accessions and the Chemotion deposit.
In total, 96,973 records are linked to a resolved structure, and 50,682 of these also carry author-reported ¹H and ¹³C NMR.
The dataset of record is the CC-BY file (190,049 records), and every record keeps its source identifier and licence.

The data are available on Hugging Face (https://huggingface.co/datasets/ilkhamfy/IRexp) and Zenodo ([10.5281/zenodo.24117617](https://doi.org/10.5281/zenodo.24117617)).
The code is in the `code/` folder of https://github.com/IlkhamFY/IRexp and archived on Zenodo ([10.5281/zenodo.24295113](https://doi.org/10.5281/zenodo.24295113)).

For technical validation, two stratified samples were checked by hand against their source documents.
In 161 main-text records, the source was found for 160, and bands were exact for 143 and an acceptable subset for 13.
In 150 supporting-information records, band lists were complete and correct for 145, and structures were correct for 90 of 100.
Automated checks found 2,131 of 2,133 sampled bands in the source text, and formula-NMR checks flag 299 of the 96,973 structure-linked records.

All authors confirm that this manuscript has not been previously published and is not under consideration elsewhere. A preprint is available on ChemRxiv ([10.26434/chemrxiv.15009750/v2](https://doi.org/10.26434/chemrxiv.15009750/v2)). The authors have approved the submitted version and agree to *Scientific Data*'s submission policies.

Best regards,  
Rodrigo A. Vargas-Hernández, on behalf of all authors  
email: vargashr@mcmaster.ca
