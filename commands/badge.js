const { SlashCommandBuilder } = require('discord.js');
const message = require('../embeds/general/embed.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('badge')
		.setDescription('Run this command to get the discord developer badge.'),
	async execute(interaction) {
		await interaction.reply('Successfully ran bot command.');
	},
};