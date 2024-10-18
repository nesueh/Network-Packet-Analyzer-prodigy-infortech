async function fetchPackets() {
    const response = await fetch('/packets');
    const packets = await response.json();
    const tableBody = document.getElementById('packet-table');
    tableBody.innerHTML = '';
    packets.forEach(packet => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${packet.src}</td>
            <td>${packet.dst}</td>
            <td>${packet.proto}</td>
            <td>${packet.payload}</td>
        `;
        tableBody.appendChild(row);
    });
}

setInterval(fetchPackets, 1000);
