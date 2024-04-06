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

        const mainStat = document.createElement('p');
        mainStat.innerHTML = `HP: ${npc.hp}, Main Stat: ${npc.main_stat}<br>Saving Throws: ${npc.saving_throws}`;


        const stats = Object.entries(npc.stat_block).map(([key, value]) => `${key}: ${value}`).join(', ');
        const statBlock = document.createElement('div');
        statBlock.innerHTML = `Stats:<br>${stats}`;


        
        const equipment = document.createElement('p');
        equipment.textContent = `Equipment: 
        ${npc.main_weapon}, ${npc.secondary_weapon}, ${npc.armor}, ${npc.trinket}, ${npc.other_item}`

        card.appendChild(name);
        card.appendChild(raceClass);
        card.appendChild(mainStat);
        card.appendChild(statBlock)
        card.appendChild(equipment)

        // Add more NPC details here as needed

        return card;
    }
});
