document.addEventListener('DOMContentLoaded', function() {
    const toggleFiltersBtn = document.getElementById('toggle-filters');
    const generateNpcsBtn = document.getElementById('generate-npcs');
    const npcContainer = document.getElementById('npc-container');
    const npcNumberInput = document.getElementById('npc-number');
    const filters = document.getElementById('npc-filters');

    // Toggle Filters Visibility
    toggleFiltersBtn.addEventListener('click', function() {
        filters.style.display = filters.style.display === 'none' ? 'block' : 'none';
    });

    // Generate NPCs
    generateNpcsBtn.addEventListener('click', function() {
        const npcNumber = parseInt(npcNumberInput.value, 10) || 5; // Default to 5 NPCs if input is invalid
        generateNPCs(npcNumber);
    });

    // Function to generate NPCs
    function generateNPCs(number) {
        fetch(`/gen_npc?number=${number}`)
            .then(response => response.json())
            .then(data => {
                npcContainer.innerHTML = ''; // Clear existing NPCs
                data.npcs_temp.npcs.forEach(npc => {
                    const npcCard = createNpcCard(npc);
                    npcContainer.appendChild(npcCard);
                });
            })
            .catch(error => console.error('Error fetching NPC data:', error));
    }

    // Function to create an NPC card
    function createNpcCard(npc) {
        const card = document.createElement('div');
        card.className = 'npc-card';

        const name = document.createElement('h3');
        name.textContent = npc.name;
        
        const raceClass = document.createElement('p');
        raceClass.textContent = `${npc.race} - ${npc.class}, Level: ${npc.level}`;

        const stats = document.createElement('p');
        stats.textContent = `Main Stat: ${npc.main_stat}, HP: ${npc.hp}`;
        
        const equipment = document.createElement('p');
        equipment.textContent = `Equipment: ${npc.main_weapon}`

        card.appendChild(name);
        card.appendChild(raceClass);
        card.appendChild(stats);
        card.appendChild(equipment)

        // Add more NPC details here as needed

        return card;
    }
});
