document.addEventListener('DOMContentLoaded', function() {
    const tableBody = document.querySelector('#filingsTable tbody');

    function fetchData() {
        fetch('/api/data')
            .then(response => response.json())
            .then(data => {
                tableBody.innerHTML = ''; // Clear existing rows
                data.forEach(row => {
                    const tr = document.createElement('tr');
                    row.forEach(cell => {
                        const td = document.createElement('td');
                        if (typeof cell === 'string' && cell.startsWith('http')) {
                            const a = document.createElement('a');
                            a.href = cell;
                            a.textContent = 'Link';
                            a.target = '_blank';
                            td.appendChild(a);
                        } else {
                            td.textContent = cell;
                        }
                        tr.appendChild(td);
                    });
                    tableBody.appendChild(tr);
                });
            });
    }

    fetchData(); // Initial fetch
    setInterval(fetchData, 300000); // Fetch new data every 5 mins
});
