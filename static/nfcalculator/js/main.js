/**
 * Created by d58560 on 11/17/2017.
 */
var index = 1;
    function insertRow(){
                var table=document.getElementById("myTable");
                var row=table.insertRow(table.rows.length);

                var cell1=row.insertCell(0);
                var t1=document.createElement("input");
                    t1.setAttribute('class', 'specialInput');
                    t1.id = "name"+index;
                    t1.type = "text";
                    cell1.appendChild(t1);

                var cell2=row.insertCell(1);
                var t2=document.createElement("input");
                    t2.setAttribute('class', 'specialInput');
                    t2.setAttribute('oninput', 'this.value = Math.abs(this.value)');
                    t2.id = "weight"+index;
                    t2.type = "number";
                    t2.min = "0";
                    cell2.appendChild(t2);
                
                var cell3=row.insertCell(2);
                var t3=document.createElement("input");
                    t3.setAttribute('class', 'specialInput');
                    t3.setAttribute('oninput', 'this.value = Math.abs(this.value)');
                    t3.id = "lipids"+index;
                    t3.type = "number";
                    t3.min = "0";
                    cell3.appendChild(t3);

                var cell4=row.insertCell(3);
                var t4=document.createElement("input");
                    t4.setAttribute('class', 'specialInput');
                    t4.setAttribute('oninput', 'this.value = Math.abs(this.value)');
                    t4.id = "saturated"+index;
                    t4.type = "number";
                    t4.min = "0";
                    cell4.appendChild(t4);

                var cell5=row.insertCell(4);
                var t5=document.createElement("input");
                    t5.setAttribute('class', 'specialInput');
                    t5.setAttribute('oninput', 'this.value = Math.abs(this.value)');
                    t5.id = "sacharides"+index;
                    t5.type = "number";
                    t5.min = "0";
                    cell5.appendChild(t5);

                var cell6=row.insertCell(5);
                var t6=document.createElement("input");
                    t6.setAttribute('class', 'specialInput');
                    t6.setAttribute('oninput', 'this.value = Math.abs(this.value)');
                    t6.id = "sugar"+index;
                    t6.type = "number";
                    t6.min = "0";
                    cell6.appendChild(t6);

                var cell7=row.insertCell(6);
                var t7=document.createElement("input");
                    t7.setAttribute('class', 'specialInput');
                    t7.setAttribute('oninput', 'this.value = Math.abs(this.value)');
                    t7.id = "protein"+index;
                    t7.type = "number";
                    t7.min = "0";
                    cell7.appendChild(t7);

                var cell8=row.insertCell(7);
                var t8=document.createElement("input");
                    t8.setAttribute('class', 'specialInput');
                    t8.setAttribute('oninput', 'this.value = Math.abs(this.value)');
                    t8.id = "salt"+index;
                    t8.type = "number";
                    t8.min = "0";
                    cell8.appendChild(t8);

                var cell9=row.insertCell(8);
                var t9=document.createElement("input");
                    t9.setAttribute('class', 'specialInput');
                    t9.id = "desc"+index;
                    t9.type = "text";
                    cell9.appendChild(t9);

          index++;

          var calculatedTable = document.getElementById("calculatedTable");
          var numberOfRows = calculatedTable.rows.length;
          console.log("numberOfRows %s:", numberOfRows);

         for (var i = numberOfRows -1 ; i > 0 ; i--) {
             calculatedTable.deleteRow(i);
         }

        var desiredCalulcationsTable = document.getElementById("desiredCalulcationsTable");
        var numberOfRowsFacts = desiredCalulcationsTable.rows.length;

        console.log("numberOfRows %s:", numberOfRows);

        for (var i = numberOfRowsFacts -1 ; i > 0 ; i--) {
            desiredCalulcationsTable.deleteRow(i);
        }

    }


var addition = 1;
function insertRecalculatedRow(name, weight, lipids, saturated, sacharides, sugar, protein, salt, desc){
            var table=document.getElementById("calculatedTable");
            var row=table.insertRow(table.rows.length);

            var cell1=row.insertCell(0);
            var t1=document.createElement("td");
                t1.id = "name"+addition;
                t1.innerHTML = name;
                cell1.appendChild(t1);

            var cell2=row.insertCell(1);
            var t2=document.createElement("td");
                t2.id = "weight"+addition;
                t2.innerHTML = weight;
                cell2.appendChild(t2);

            var cell3=row.insertCell(2);
            var t3=document.createElement("td");
                t3.id = "lipids"+addition;
                t3.innerHTML = lipids;
                cell3.appendChild(t3);

            var cell4=row.insertCell(3);
            var t4=document.createElement("td");
                t4.id = "saturated"+addition;
                t4.innerHTML = saturated;
                cell4.appendChild(t4);

            var cell5=row.insertCell(4);
            var t5=document.createElement("td");
                t5.id = "sacharides"+addition;
                t5.innerHTML = sacharides;
                cell5.appendChild(t5);

            var cell6=row.insertCell(5);
            var t6=document.createElement("td");
                t6.id = "sugar"+addition;
                t6.innerHTML = sugar;
                cell6.appendChild(t6);

            var cell7=row.insertCell(6);
            var t7=document.createElement("td");
                t7.id = "protein"+addition;
                t7.innerHTML = protein;
                cell7.appendChild(t7);

            var cell8=row.insertCell(7);
            var t8=document.createElement("td");
                t8.id = "salt"+addition;
                t8.innerHTML = salt;
                cell8.appendChild(t8);

            var cell9=row.insertCell(8);
            var t9=document.createElement("td");
                t9.id = "desc"+addition;
                t9.innerHTML = desc;
                cell9.appendChild(t9);

      addition++;

}


var plus = 1;
function insertFinalNutritionRow(weight, lipids, saturated, sacharides, sugar, protein, salt, kilojouls,kilocals){
            var table=document.getElementById("desiredCalulcationsTable");
            var row=table.insertRow(table.rows.length);

            var cell1=row.insertCell(0);
            var t1=document.createElement("td");
                t1.id = "weight"+plus;
                t1.innerHTML = weight;
                cell1.appendChild(t1);

            var cell2=row.insertCell(1);
            var t2=document.createElement("td");
                t2.id = "lipids"+plus;
                t2.innerHTML = lipids;
                cell2.appendChild(t2);

            var cell3=row.insertCell(2);
            var t3=document.createElement("td");
                t3.id = "saturated"+plus;
                t3.innerHTML = saturated;
                cell3.appendChild(t3);

            var cell4=row.insertCell(3);
            var t4=document.createElement("td");
                t4.id = "sacharides"+plus;
                t4.innerHTML = sacharides;
                cell4.appendChild(t4);

            var cell5=row.insertCell(4);
            var t5=document.createElement("td");
                t5.id = "sugar"+plus;
                t5.innerHTML = sugar;
                cell5.appendChild(t5);

            var cell6=row.insertCell(5);
            var t6=document.createElement("td");
                t6.id = "protein"+plus;
                t6.innerHTML = protein;
                cell6.appendChild(t6);

            var cell7=row.insertCell(6);
            var t7=document.createElement("td");
                t7.id = "salt"+plus;
                t7.innerHTML = salt;
                cell7.appendChild(t7);

            var cell8=row.insertCell(7);
            var t8=document.createElement("td");
                t8.id = "kilojouls"+plus;
                t8.innerHTML = kilojouls;
                cell8.appendChild(t8);

            var cell9=row.insertCell(8);
            var t9=document.createElement("td");
                t9.id = "kilocals"+plus;
                t9.innerHTML = kilocals;
                cell9.appendChild(t9);

      plus++;

}




function myDeleteFunction() {

    var table = document.getElementById("myTable");
    var lastRowIndex = table.rows.length-1;
    if (lastRowIndex > 0) {
        document.getElementById("myTable").deleteRow(lastRowIndex);
    }

    // per real weights
    var calculatedTable = document.getElementById("calculatedTable");
    var numberOfRows = calculatedTable.rows.length;

    console.log("numberOfRows %s:", numberOfRows);

    for (var i = numberOfRows -1 ; i > 0 ; i--) {
        calculatedTable.deleteRow(i);
    }


    var desiredCalulcationsTable = document.getElementById("desiredCalulcationsTable");
    var numberOfRowsFacts = desiredCalulcationsTable.rows.length;

    console.log("numberOfRows %s:", numberOfRows);

    for (var i = numberOfRowsFacts -1 ; i > 0 ; i--) {
        desiredCalulcationsTable.deleteRow(i);
    }
}

function getAllInputIds() {
    var table, inputs, arr;

    table = document.getElementById( 'myTable' );
    inputs = table.querySelectorAll( 'input' );
    arr = [].slice.call( inputs ).map(function ( node ) {
        return node.id;
    });

    // alert( arr );

    // for (i = 0; i < arr.length; i++) {
    //     console.log("ID: %s => value: %s", arr[i], document.getElementById(arr[i]).value);
    // }

    return arr
}

function collectDataFromColumns(rows, col, shift, arr) {
            var vec = [];
            for (var i = 0; i < rows -1 ; i++) {
                var ind = (i * (col)) + shift;
                //console.log("ind: %s", shift);
                vec.push(document.getElementById(arr[ind]).value);
                }
            return vec;
        }
function calculateProductPerNGramms(gr, rows, weightVector, substanceVector) {
            var grams = gr;
            var recalculated = [];
            for (var i = 0; i < rows -1 ; i++){
                var temp = (parseFloat(weightVector[i]) * parseFloat(substanceVector[i])) / parseFloat(grams);
                recalculated.push(temp);
            }
            return recalculated;
        }

function processDataFromTable() {

        // inArray => one-dimensional array with all the values from
        //               the table

        inArray = getAllInputIds();

        var table = document.getElementById("myTable");
        var rows = table.rows.length;
        var col = table.rows[0].cells.length;
        var grams = 100;


        var calculatedTable = document.getElementById("calculatedTable");
        var numberOfRows = calculatedTable.rows.length;
        console.log("numberOfRows %s:", numberOfRows);

        for (var i = numberOfRows -1 ; i > 0 ; i--) {
             calculatedTable.deleteRow(i);
            }

        var desiredCalulcationsTable = document.getElementById("desiredCalulcationsTable");
        var numberOfRowsFacts = desiredCalulcationsTable.rows.length;

        console.log("numberOfRows %s:", numberOfRows);

        for (var i = numberOfRowsFacts -1 ; i > 0 ; i--) {
            desiredCalulcationsTable.deleteRow(i);
        }


        console.log("Rows: %s => Columns: %s", rows, col);
        var nameArrayFilled = collectDataFromColumns(rows, col, 0, inArray);
        var weightArrayFilled = collectDataFromColumns(rows, col, 1, inArray);
        var lipidsArrayFilled = collectDataFromColumns(rows, col, 2, inArray);
        var saturatedArrayFilled = collectDataFromColumns(rows, col, 3, inArray);
        var sacharidesArrayFilled = collectDataFromColumns(rows, col, 4, inArray);
        var sugarArrayFilled = collectDataFromColumns(rows, col, 5, inArray);
        var proteinArrayFilled = collectDataFromColumns(rows, col, 6, inArray);
        var saltArrayFilled = collectDataFromColumns(rows, col, 7, inArray);
        var descArrayFilled = collectDataFromColumns(rows, col, 8, inArray);

        // Calculate total product weight
        var totalProductWeight = weightArrayFilled.reduce(function(a, b) { return parseFloat(a) + parseFloat(b); }, 0);
        console.log("Weight: %s", totalProductWeight)

        // recalculated values per 100 grams
        var lipidsArrayRecalculated = calculateProductPerNGramms(grams, rows, weightArrayFilled, lipidsArrayFilled);
        var saturatedArrayRecalculated = calculateProductPerNGramms(grams, rows, weightArrayFilled, saturatedArrayFilled);
        var sacharidesArrayRecalculated = calculateProductPerNGramms(grams, rows, weightArrayFilled, sacharidesArrayFilled);
        var sugarArrayRecalculated = calculateProductPerNGramms(grams, rows, weightArrayFilled, sugarArrayFilled);
        var proteinArrayRecalculated = calculateProductPerNGramms(grams, rows, weightArrayFilled, proteinArrayFilled);
        var saltArrayRecalculated = calculateProductPerNGramms(grams, rows, weightArrayFilled, saltArrayFilled);

        var lipidsWeight = lipidsArrayRecalculated.reduce(function(a, b) { return parseFloat(a) + parseFloat(b); }, 0);
        var saturatedWeight = saturatedArrayRecalculated.reduce(function(a, b) { return parseFloat(a) + parseFloat(b); }, 0);
        var sacharidesWeight = sacharidesArrayRecalculated.reduce(function(a, b) { return parseFloat(a) + parseFloat(b); }, 0);
        var sugarWeight = sugarArrayRecalculated.reduce(function(a, b) { return parseFloat(a) + parseFloat(b); }, 0);
        var proteinWeight = proteinArrayRecalculated.reduce(function(a, b) { return parseFloat(a) + parseFloat(b); }, 0);
        var saltWeight = saltArrayRecalculated.reduce(function(a, b) { return parseFloat(a) + parseFloat(b); }, 0);

        var lipidsPerNGrams = (parseFloat(grams) * parseFloat(lipidsWeight)) / totalProductWeight;
        var saturatedPerNGrams = (parseFloat(grams) * parseFloat(saturatedWeight)) / totalProductWeight;
        var sacharidesPerNGrams = (parseFloat(grams) * parseFloat(sacharidesWeight)) / totalProductWeight;
        var sugarPerNGrams = (parseFloat(grams) * parseFloat(sugarWeight)) / totalProductWeight;
        var proteinPerNGrams = (parseFloat(grams) * parseFloat(proteinWeight)) / totalProductWeight;
        var saltPerNGrams = (parseFloat(grams) * parseFloat(saltWeight)) / totalProductWeight;

        var kiloJouls = (17 * proteinPerNGrams) + (37 * lipidsPerNGrams) + (17 * sacharidesPerNGrams);
        var kiloCals = (4 * proteinPerNGrams) + (9 * lipidsPerNGrams) + (4 * sacharidesPerNGrams);

        console.log("kiloJouls %s", kiloJouls);
        console.log("kiloCals: %s", kiloCals);

        console.log("lipidsPerNGrams: %s", lipidsPerNGrams);
        console.log("saturatedPerNGrams: %s", saturatedPerNGrams);
        console.log("sacharidesPerNGrams: %s", sacharidesPerNGrams);
        console.log("sugarPerNGrams: %s", sugarPerNGrams);
        console.log("proteinPerNGrams: %s", proteinPerNGrams);
        console.log("saltPerNGrams: %s", saltPerNGrams);

        // console.log("lipidsWeight: %s", lipidsWeight);
        // console.log("saturatedWeight: %s", saturatedWeight);
        // console.log("sacharidesWeight: %s", sacharidesWeight);
        // console.log("sugarWeight: %s", sugarWeight);
        // console.log("proteinWeight: %s", proteinWeight);
        // console.log("saltWeight: %s", saltWeight);


        obj = document.getElementById('secretId');
        obj.style.display = "";

        // Creating tables with recalculated values
        for (var i = 0; i < rows -1 ; i++){
            insertRecalculatedRow(
                nameArrayFilled[i],
                weightArrayFilled[i],
                lipidsArrayRecalculated[i],
                saturatedArrayRecalculated[i],
                sacharidesArrayRecalculated[i],
                sugarArrayRecalculated[i],
                proteinArrayRecalculated[i],
                saltArrayRecalculated[i],
                descArrayFilled[i]);
        }

        // un-hiding Final Nutrition Facts
        obj = document.getElementById('desiredCalulcationsDIV');
        obj.style.display = "";

        insertFinalNutritionRow(
                totalProductWeight.toFixed(2),
                lipidsPerNGrams.toFixed(2),
                saturatedPerNGrams.toFixed(2),
                sacharidesPerNGrams.toFixed(2),
                sugarPerNGrams.toFixed(2),
                proteinPerNGrams.toFixed(2),
                saltPerNGrams.toFixed(2),
                kiloJouls.toFixed(2),
                kiloCals.toFixed(2)
        );

        console.log("**********************************");
        console.log("      Start over!");
        console.log("**********************************");


}






