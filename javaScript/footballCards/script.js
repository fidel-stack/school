const footballTeam = {
  team: "Ironfield United FC",
  year: 1999,
  headCoach: "Alex Turner",
  players: [
    {name: "Daniel Moore", position: "goalkeeper", isCaptain: false},
    {name: "Lucas Bennet", position: "goalkeeper", isCaptain: false},
    {name: "Ryan Cole", position: "defender", isCaptain: false},
    {name: "Marco Silva", position: "defender", isCaptain: false},
    {name: "Tomas Novak", position: "defender", isCaptain: false},
    {name: "Ethan Brooks", position: "defender", isCaptain: false},
    {name: "Victor Mensah", position: "defender", isCaptain: false},
    {name: "Jonas Lindhom", position: "defender", isCaptain: false},
    {name: "Oliver Grant", position: "midfielder", isCaptain: true},
    {name: "Mateo Ruiz", position: "midfielder", isCaptain: false},
    {name: "Samir Haddad", position: "midfielder", isCaptain: false},
    {name:"Patrick O'Neil", position: "midfielder", isCaptain: false},
    {name: "Nico Bauer", position: "midfielder", isCaptain: false},
    {name: "Luis Fernandez", position: "midfielder", isCaptain: false},
    {name: "Jordan King", position: "forward", isCaptain: false},
    {name: "Adrian Kovacs", position: "forward", isCaptain: false},
    {name: "Michael Adeyemi", position: "forward", isCaptain: false},
    {name: "Felix Romano", position: "forward", isCaptain: false},
    {name: "Callum Price", position: "forward", isCaptain: false}
  ]
}
document.getElementById("team").textContent = footballTeam.team;
document.getElementById("year").textContent = footballTeam.year;
document.getElementById("head-coach").textContent = footballTeam.headCoach;
const playersCards = document.getElementById("player-cards");

function renderPlayers (playersArray){
  playersCards.innerHTML = playersArray.map(player =>
`<div class="player-card">
<h2>${player.name}${player.isCaptain ? ' (Captain)' : ''}</h2>
 <p>Position: ${player.position}</p>
 </div>`)
 .join('');
}

function getPlayers (specPlayers){
  const positionPlayer = specPlayers === "all" ?  footballTeam.players : 
  footballTeam.players.filter(({position}) => position === specPlayers);
  return positionPlayer;
}

renderPlayers(footballTeam.players);
players.addEventListener("change", () =>{
  renderPlayers(getPlayers(players.value));
})
 