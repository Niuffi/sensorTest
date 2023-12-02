function start() {
    const n = document.getElementById("n");
    const AS7262 = document.getElementById("AS7262");
    const AS7341 = document.getElementById("AS7341");



    console.log("" +
        "n: " + n.value + "\n" +"" +
        "AS7262: " + AS7262.checked + "\n" +
        "AS7341: " + AS7341.checked + "\n");
}

async function getFiles() {
    // AS7672_2023-01-01_12:47:11_10.csv
    let files = []

    const response = await fetch('/api/files').then(response => response.json());
    console.log(response);

    response.forEach(fileName => {
        fileNameNoExtension = fileName.split(".")[0];
        fileNameSplited = fileNameNoExtension.split("_");
        files.push({
            sensor: fileNameSplited[0],
            date: fileNameSplited[1],
            time: fileNameSplited[2],
            samples: fileNameSplited[3],
            originalName: fileName
        });
    });
    console.log(files);

    const table = document.getElementById("filesTable");
    const tableBody = document.createElement("tbody");
    tableBody.id = "filesTableBody";
    table.appendChild(tableBody);

    files.forEach(file => {
        const row = document.createElement("tr");
        const sensor = document.createElement("td");
        const time = document.createElement("td");
        const date = document.createElement("td");
        const samples = document.createElement("td");
        const button = document.createElement("button");

        sensor.innerText = file.sensor;
        date.innerText = file.date;
        time.innerText = file.time;
        samples.innerText = file.samples;
        button.innerText = "Download";
        button.onclick = () => downloadFile(file.originalName);

        row.appendChild(sensor);
        row.appendChild(time);
        row.appendChild(date);
        row.appendChild(samples);
        row.appendChild(button);
        tableBody.appendChild(row);
    });


}

async function downloadFile(fileName) {
    const fileContent = await fetch('/api/download/' + fileName);
    const fileBlob = await fileContent.blob();
    const fileUrl = URL.createObjectURL(fileBlob);
    const link = document.createElement('a');
    link.href = fileUrl;
    link.download = fileName;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);

}

function saveConfigToCookies() {
    const n = document.getElementById("n");
    const AS7262 = document.getElementById("AS7262");
    const AS7341 = document.getElementById("AS7341");

    document.cookie = "n=" + n.value;
    document.cookie = "AS7262=" + AS7262.checked;
    document.cookie = "AS7341=" + AS7341.checked;
}

function loadConfigFromCookies() {
    const elementsMap = {
        n: document.getElementById("n"),
        AS7262: document.getElementById("AS7262"),
        AS7341: document.getElementById("AS7341")
    };

    const cookies = document.cookie.split(";");

    cookies.forEach(cookie => {
        const [cookieName, cookieValue] = cookie.split("=").map(c => c.trim());
        if (elementsMap.hasOwnProperty(cookieName)) {
            if (cookieName === 'n') {
                elementsMap[cookieName].value = cookieValue;
            } else {
                elementsMap[cookieName].checked = cookieValue === "true";
            }
        }
    });
}

function onLoad() {
    loadConfigFromCookies();
    getFiles();
}

