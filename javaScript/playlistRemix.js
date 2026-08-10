const playlists = [
  [
    {
      trackId: "trk101",
      artist: "Velvet Comet",
      title: "Crimson Afterglow",
      votes: 5,
      bpm: 122
    },
    {
      trackId: "trk102",
      artist: "Neon Harbor",
      title: "Static Horizon",
      votes: 2,
      bpm: 108
    },
    {
      trackId: "trk103",
      artist: "Lunar Arcade",
      title: "Midnight Frequency",
      votes: 4,
      bpm: 128
    }
  ],
  [
    {
      trackId: "trk201",
      artist: "Solar Echo",
      title: "Glass Skyline",
      votes: 3,
      bpm: 115
    },
    {
      trackId: "trk202",
      artist: "Velvet Comet",
      title: "Satellite Hearts",
      votes: 6,
      bpm: 124
    }
  ]
];

function flattenPlaylists (arr) {
  if (!Array.isArray(arr)) return [];
  const results = [];
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[i].length; j++){
      results.push({
      trackId: arr[i][j].trackId,
      artist: arr[i][j].artist,
      title: arr[i][j].title,
      votes: arr[i][j].votes,
      bpm: arr[i][j].bpm,
      source: [i, j]
      });
    };
  }

  return results;
}
function scoreTracks (arr) {
  const results = []
  for (const track of arr) {
    results.push({
      trackId: track.trackId,
      artist: track.artist,
      title: track.title,
      votes: track.votes,
      bpm: track.bpm,
      source: track.source,
      score: track.votes * 10 - Math.abs(track.bpm - 120)
    })
  }
  return results;
}

function dedupeTracks (arr) {
  const result = [];
  for (let i = 0; i < arr.length; i++) {
    if (!result.some(track => track.trackId === arr[i].trackId)) {
      result.push(arr[i])
    }
  }
  return result;
}

function enforceArtistQuota (track, num) {
  const result = [];
  const artistCount = {};
  for (let i = 0; i < track.length; i++) {
    if (artistCount[track[i].artist] === undefined) {
      artistCount[track[i].artist] = 0;
      }
      if (artistCount[track[i].artist] < num) {
        result.push(track[i])
        artistCount[track[i].artist] ++;
      }
  }
    return result;
}


function buildSchedule (tracks) {
  const result = [];
  for (let i = 0; i < tracks.length; i++) {
    result.push({
      slot: i + 1,
      trackId: tracks[i].trackId
    })
  }
  return result;
}

function remixPlaylist(playlists, maxPerArtist) {
  const flattened = flattenPlaylists(playlists);
  const score = scoreTracks(flattened)
  const unique = dedupeTracks(score);
  const quota = enforceArtistQuota(unique, maxPerArtist);
  const schedule = buildSchedule(quota);
  return schedule;
}