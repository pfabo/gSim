#-----------------------------------------------------------------------
cd ./100_spice_basic
pwd

for file in 100 102  
do
    python3 $file'_prg.py' 
    gschem -p -o $file'_doc.ps' -s ../print.scm $file'_circ.sch' 
    ps2pdf -sPAPERSIZE=a4 $file'_doc.ps' 
    rm $file'_doc.ps' 
done
rm -f -r ./tmp
cd ..
#-----------------------------------------------------------------------
cd ./200_spice_rlc
pwd

for file in 200 201 203 204 205 
do
    python3 $file'_prg.py' 
    gschem -p -o $file'_doc.ps' -s ../print.scm $file'_circ.sch' 
    ps2pdf -sPAPERSIZE=a4 $file'_doc.ps' 
    rm $file'_doc.ps' 
done
rm -f -r ./tmp
cd ..
#-----------------------------------------------------------------------
cd ./250_spice_filters
pwd

for file in 250 251 252 253  
do
    python3 $file'_prg.py' 
    gschem -p -o $file'_doc.ps' -s ../print.scm $file'_circ.sch' 
    ps2pdf -sPAPERSIZE=a4 $file'_doc.ps' 
    rm $file'_doc.ps' 
done
rm -f -r ./tmp
cd ..
#-----------------------------------------------------------------------
cd ./300_spice_diode_bjt
pwd

for file in 300 301 302 303 304 305 306 307 308 309 310 311  
do
    python3 $file'_prg.py' 
    gschem -p -o $file'_doc.ps' -s ../print.scm $file'_circ.sch' 
    ps2pdf -sPAPERSIZE=a4 $file'_doc.ps' 
    rm $file'_doc.ps' 
done
rm -f -r ./tmp
cd ..
#-----------------------------------------------------------------------
cd ./350_spice_ttl
pwd

for file in 350 351 352 353   
do
    python3 $file'_prg.py' 
    gschem -p -o $file'_doc.ps' -s ../print.scm $file'_circ.sch' 
    ps2pdf -sPAPERSIZE=a4 $file'_doc.ps' 
    rm $file'_doc.ps' 
done
rm -f -r ./tmp
cd ..
#-----------------------------------------------------------------------
cd ./450_spice_signal
pwd

for file in 450 451   
do
    python3 $file'_prg.py' 
    gschem -p -o $file'_doc.ps' -s ../print.scm $file'_circ.sch' 
    ps2pdf -sPAPERSIZE=a4 $file'_doc.ps' 
    rm $file'_doc.ps' 
done
rm -f -r ./tmp
cd ..
#-----------------------------------------------------------------------
cd ./500_xspice_analog
pwd

for file in 500 501 502 503   
do
    python3 $file'_prg.py' 
    gschem -p -o $file'_doc.ps' -s ../print.scm $file'_circ.sch' 
    ps2pdf -sPAPERSIZE=a4 $file'_doc.ps' 
    rm $file'_doc.ps' 
done
rm -f -r ./tmp
cd ..
#-----------------------------------------------------------------------
cd ./550_xspice_digital
pwd

for file in 550 551  
do
    python3 $file'_prg.py' 
    gschem -p -o $file'_doc.ps' -s ../print.scm $file'_circ.sch' 
    ps2pdf -sPAPERSIZE=a4 $file'_doc.ps' 
    rm $file'_doc.ps' 
done
rm -f -r ./tmp
cd ..
#-----------------------------------------------------------------------
cd ./600_xspice_mixed
pwd

for file in 600 602  
do
    python3 $file'_prg.py' 
    gschem -p -o $file'_doc.ps' -s ../print.scm $file'_circ.sch' 
    ps2pdf -sPAPERSIZE=a4 $file'_doc.ps' 
    rm $file'_doc.ps' 
done
rm -f -r ./tmp
cd ..
#-----------------------------------------------------------------------
cd ./700_xspice_hybrid
pwd

for file in 700 701 702
do
    python3 $file'_prg.py' 
    gschem -p -o $file'_doc.ps' -s ../print.scm $file'_circ.sch' 
    ps2pdf -sPAPERSIZE=a4 $file'_doc.ps' 
    rm $file'_doc.ps' 
done
rm -f -r ./tmp
cd ..
#-----------------------------------------------------------------------

