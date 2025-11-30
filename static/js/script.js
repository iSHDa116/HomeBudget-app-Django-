function SortTable(columnIndex){
    const table = document.getElementById("myTable");
    let isSwich = true;
    let dir = "asc";

    while(isSwich){
        isSwich = false;
        let rows = table.rows;

        for(let i = 1; i < rows.length - 1; i++ ){
            let shouldSwich = false;
            
            let x = rows[i].getElementByTagName("TD")[columnIndex];
            let y = rows[i + 1].getElementByTagName("TD")[columnIndex];

            let xContent = isNaN(x.innerHTML) ? x.innerHTML.toLowerCase() : Number(x.innerHTML);
            let yContent = isNaN(y.innerHTML) ? y.innerHTML.toLowerCase() : Number(y.innerHTML);

            if ((direction === "asc" && xContent > yContent) ||
                (direction === "desc" && xContent < yContent)) {
                shouldSwitch = true;
                break;
            }
        }

        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        } else {
            if (direction === "asc") {
                direction = "desc";
                switching = true;
            }
        }
    }
}
