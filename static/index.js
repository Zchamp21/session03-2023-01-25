function onload() {

    function update() {
        let guest = document.getElementById("guest");
        let record = document.getElementById("record");
        
        if (guest.value && record.value) {
            const newNode = document.createElement("li");
            const text = `${guest.value}: ${record.value}`;
            const textNode = document.createTextNode(text);
            newNode.appendChild(textNode);

            let list = document.getElementById("albumList");
            list.appendChild(newNode);
        }

        guest.value = "";
        record.value = "";
        // console.log("updating");
        // let guest = document.getElementById("guest");
        // console.log(guest.value);
        // let form = document.querySelector("form");
        // console.log(form.guest);
    }

    let btn = document.getElementById("submit");
    btn.onclick = update;
}

window.addEventListener("load", onload);