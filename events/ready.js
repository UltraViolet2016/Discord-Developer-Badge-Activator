const { guildName } = require('../config.json');
const { ActivityType } = require('discord.js');

module.exports = {
	name: 'ready',
	once: true,
	async execute(client) {
		console.log(`[DiscordBadge] Successfully logged into ${client.user.tag}`);
		client.user.setActivity(`${guildName}`, { type: ActivityType.Watching });
		client.user.setStatus('dnd');

	},
};