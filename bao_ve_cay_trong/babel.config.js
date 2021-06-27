module.exports = {
	presets: ['module:metro-react-native-babel-preset'],
	plugins: [
		[
			'module-resolver',
			{
				root: ['.', './src'],
				/* alias: {
					'*': './*',
				}, */
			},
		],
		[
			'babel-plugin-inline-import',
			{
				extensions: ['.svg'],
			},
		],
		[
			'module:react-native-dotenv',
			{
				moduleName: '@env',
				path: '.env',
				blacklist: null,
				whitelist: null,
				safe: false,
				allowUndefined: true,
			},
		],
	],
};
