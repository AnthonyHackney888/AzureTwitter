module.exports = async function (context, req) {
    context.log('Generating Nonsense...');
    let now = new Date();
    context.res = {
        body: "The date and time is: " + now.toISOString()+ "T"+ now.toTimeString()
    };
};