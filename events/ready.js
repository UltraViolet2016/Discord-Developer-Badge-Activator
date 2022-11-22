const { ActivityType } = require('discord.js');

module.exports = {
	name: 'ready',
	once: true,
	async execute(client) {
		console.log(`[DiscordBadge] Successfully logged into ${client.user.tag}`);
		client.user.setActivity(`Dark's Developer Badge Activator`, { type: ActivityType.Playing});
		client.user.setStatus('dnd');

	},
};