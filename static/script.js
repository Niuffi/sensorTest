async function start() {
    const n = document.getElementById("n");
    const AS7262 = document.getElementById("AS7262");
    const AS7341 = document.getElementById("AS7341");
    const AS7265x = document.getElementById("AS7265x");
    let AS7262param = 0;
    let AS7341param = 0;
    let AS7265xparam = 0;


    if (AS7262.checked === false && AS7341.checked === false && AS7265x.checked === false) {
        alert("Please select at least one sensor to start the measurement.");
    }

    if (AS7262.checked === true) {
        AS7262param = 1;
    }

    if (AS7341.checked === true) {
        AS7341param = 1;
    }

    if (AS7265x.checked === true) {
        AS7265xparam = 1;
    }

    await fetch('/api/start?n=' + n.value +
        '&AS7262=' + AS7262param +
        '&AS7341=' + AS7341param +
        '&AS7265x=' + AS7265xparam);
}

async function getFiles() {
    let files = []

    const response = await fetch('/api/files').then(response => response.json());

    response.forEach(fileName => {
        const fileNameNoExtension = fileName.split(".")[0];
        const fileNameSplit = fileNameNoExtension.split("_");
        files.push({
            sensor: fileNameSplit[0],
            date: fileNameSplit[1],
            time: fileNameSplit[2].replaceAll("-", ":"),
            samples: fileNameSplit[3],
            originalName: fileName
        });
    });

    files.sort((a, b) => {
        if (a.date > b.date) {
            return -1;
        } else if (a.date < b.date) {
            return 1;
        } else {
            if (a.time > b.time) {
                return -1;
            } else if (a.time < b.time) {
                return 1;
            } else {
                return 0;
            }
        }
    });

    const table = document.getElementById("filesTable");
    const tableBody = document.createElement("tbody");
    table.innerHTML = "";
    tableBody.id = "filesTableBody";
    table.appendChild(tableBody);

    const header = document.createElement("tr");
    const sensorHeader = document.createElement("th");
    const timeHeader = document.createElement("th");
    const dateHeader = document.createElement("th");
    const samplesHeader = document.createElement("th");
    const downloadHeader = document.createElement("th");
    const deleteHeader = document.createElement("th");

    sensorHeader.innerText = "Sensor";
    timeHeader.innerText = "Time";
    dateHeader.innerText = "Date";
    samplesHeader.innerText = "Samples";
    downloadHeader.innerText = "";
    deleteHeader.innerText = "";

    header.appendChild(sensorHeader);
    header.appendChild(timeHeader);
    header.appendChild(dateHeader);
    header.appendChild(samplesHeader);
    header.appendChild(downloadHeader);
    header.appendChild(deleteHeader);

    tableBody.appendChild(header);


    files.forEach(file => {
        const row = document.createElement("tr");
        const sensor = document.createElement("td");
        const time = document.createElement("td");
        const date = document.createElement("td");
        const samples = document.createElement("td");
        const downloadButton = document.createElement("button");
        const deleteButton = document.createElement("button");

        sensor.innerText = file.sensor;
        date.innerText = file.date;
        time.innerText = file.time;
        samples.innerText = file.samples;
        downloadButton.innerText = "Download";
        downloadButton.onclick = () => downloadFile(file.originalName);
        deleteButton.innerText = "Delete";
        deleteButton.onclick = () => deleteFile(file.originalName);

        row.appendChild(sensor);
        row.appendChild(time);
        row.appendChild(date);
        row.appendChild(samples);
        row.appendChild(downloadButton);
        row.appendChild(deleteButton);
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

async function deleteFile(fileName) {
    const confirmation = confirm("Are you sure you want to delete " + fileName + "?");

    if (confirmation) {
        await fetch('/api/file/' + fileName, {method: 'DELETE'});
        await getFiles();
    }
}

function saveConfigToCookies() {
    const n = document.getElementById("n");
    const AS7262 = document.getElementById("AS7262");
    const AS7341 = document.getElementById("AS7341");
    const AS7265x = document.getElementById("AS7265x");

    document.cookie = "n=" + n.value;
    document.cookie = "AS7262=" + AS7262.checked;
    document.cookie = "AS7341=" + AS7341.checked;
    document.cookie = "AS7265x=" + AS7265x.checked;
}

function loadConfigFromCookies() {
    const elementsMap = {
        n: document.getElementById("n"),
        AS7262: document.getElementById("AS7262"),
        AS7341: document.getElementById("AS7341"),
        AS7265x: document.getElementById("AS7265x")
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

async function onLoad() {
    loadConfigFromCookies();
    await getFiles();
}

