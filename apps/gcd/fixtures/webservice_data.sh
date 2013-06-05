FILENAME=apps/gcd/fixtures/webservices_data.yaml
INVOCATION="./manage.py dumpdata"
FORMAT="yaml"

set -x

echo "# Publishers" > $FILENAME
echo "" >> $FILENAME
$INVOCATION -f 'id=78' gcd.publisher --format $FORMAT >> $FILENAME
echo "" >> $FILENAME
echo "" >> $FILENAME

echo "# Brands" >> $FILENAME
echo "" >> $FILENAME
$INVOCATION -f 'parent=78'  gcd.brand --format $FORMAT >> $FILENAME
echo "" >> $FILENAME
echo "" >> $FILENAME

echo "# Ind Publishers" >> $FILENAME
echo "" >> $FILENAME
$INVOCATION -f 'parent=78' gcd.indiciapublisher --format $FORMAT >> $FILENAME
echo "" >> $FILENAME
echo "" >> $FILENAME

echo "# Issues" >> $FILENAME
echo "" >> $FILENAME
$INVOCATION -f 'parent=78' gcd.issue --format $FORMAT >> $FILENAME
echo "" >> $FILENAME
echo "" >> $FILENAME

~/bin/yamldump "$FILENAME"