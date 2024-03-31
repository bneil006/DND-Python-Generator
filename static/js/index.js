function fetchNpcNames() {
    fetch('/npc_generator?number=5')
    fetch('/npc_names')
    .then(response => response.json())
    .then(data => {
        const npcNamesList = document.getElementById('npc-names-list');
        if (data.npc_names && data.npc_names.length > 0) {
        const list = document.createElement('ul');
        data.npc_names.forEach(name => {
            const item = document.createElement('li');
            item.textContent = name;
            list.appendChild(item);
        });
        npcNamesList.appendChild(list);
        } else {
        npcNamesList.textContent = 'No NPC names found.';
        }
    })
    .catch(error => {
        console.error('Error fetching NPC names:', error);
        document.getElementById('npc-names-list').textContent = 'Failed to load NPC names.';
    });
}
