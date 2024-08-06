db = db.getSiblingDB('ragstone');

// Create users collection and insert admin user
db.createCollection('users');
db.users.insertOne({
  username: "admin",
  hashed_password: "$2b$12$divoCBTGayIj/K7SsvwGyeLDn1dfmXgh5HySTsJo5fjQVxAQX1rua" // Hashed value of "Eqix1998@"
});

// Create populated_files collection
db.createCollection('populated_files');

// Create settings collection and insert default settings
db.createCollection('settings');
db.settings.insertOne({
  model: 'llama3.1',
  chunk_size: 1024,
  chunk_overlap: 300,
  prompt_template: `You are an intelligent assistant called Ragstone helping potential & current customers to answer their queries.\nGive simple and direct answers without additional statements. Do not append any According to the provided context, just give answer directly.\nDO NOT make up answers, answer the question based ONLY on the following context:\n`
});