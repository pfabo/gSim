#-----------------------------------------------------------------------
cd ./1300_xyce_npn
pwd

for file in 1300 1301 1302 1303 1304 1305 1306 1307 1308 1309 1310 1311 
do
    python3 $file'_prg.py' 
    gschem -p -o $file'_doc.ps' -s ../print.scm $file'_circ.sch' 
    ps2pdf -sPAPERSIZE=a4 $file'_doc.ps' 
    rm $file'_doc.ps' 
done
rm -f -r ./tmp
cd ..
#-----------------------------------------------------------------------
cd ./1500_xyce_analog
pwd

for file in 1500 1501 1502 
do
    python3 $file'_prg.py' 
    gschem -p -o $file'_doc.ps' -s ../print.scm $file'_circ.sch' 
    ps2pdf -sPAPERSIZE=a4 $file'_doc.ps' 
    rm $file'_doc.ps' 
done
rm -f -r ./tmp
cd ..
#-----------------------------------------------------------------------

cd ./1200_xyce_rlc
pwd

for file in 1205 1250 1251 1253 1254 
do
    python3 $file'_prg.py' 
    gschem -p -o $file'_doc.ps' -s ../print.scm $file'_circ.sch' 
    ps2pdf -sPAPERSIZE=a4 $file'_doc.ps' 
    rm $file'_doc.ps' 
done
rm -f -r ./tmp
cd ..
#-----------------------------------------------------------------------

