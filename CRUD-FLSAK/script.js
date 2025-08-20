async function add(params) {
    const a = document.getElementById("num1").value;
    const b = document.getElementById("num2").value;

    const response = await fetch("http://127.0.0.1:5000", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ a: parseFloat(a), b: parseFloat(b) }),
    });

    const data = await response.json();
    document.getElementById("result").innerText = `Result: ${data.result}`;
}

async function get_records(){
    const response = await fetch("http://127.0.0.1:5000/list");
    data = await response.json();
    console.log(data);

    const tableBody = document.getElementById("tableBody");

    tableBody.innerHTML = "";
    let sno = 1;

    for (const id in data){
        const rowData = data[id];
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${sno++}</td>
            <td>${rowData.num1}</td>
            <td>${rowData.num2}</td>
            <td>${rowData.result}</td> 
            <td><button onclick="delete_record(${id})">Delete</td>
            <td><button onclick="edit_record(${id})">Edit</td>
            `;
        tableBody.appendChild(row);
    }

}
function delete_record(id){
    fetch(`http://127.0.0.1:5000/delete/${id}`,{
        method: "DELETE",
    });
}

async function edit_record(id) {
    response = await fetch(`http://127.0.0.1:5000/list/${id}`);
    data = await response.text();
    alert(`Edit the record with ID ${data[id]}: ${data[id]["num1"]} and ${data[id]["num2"]}`);
    const newData = prompt("Enter new data: for Num 1", data[id]["num1"]);
    const newData2 = prompt("Enter new data: for Num 2", data[id]["num2"]);
    if(newData && newData2){
        fetch(`http://127.0.0.1:5000/update/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({a: newData, b: newData2})
        });
    }

}
