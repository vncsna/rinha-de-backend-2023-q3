CREATE TABLE IF NOT EXISTS person (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    apelido VARCHAR(32) UNIQUE NOT NULL,
    nome VARCHAR(100) NOT NULL,
    nascimento DATE NOT NULL,
    stack VARCHAR(32)[]
);

DO $$
BEGIN
    INSERT INTO person (apelido, nome, nascimento, stack) VALUES
        ('john_doe', 'John Doe', '1980-01-15', ARRAY['Python', 'SQL', 'JavaScript']),
        ('alice_smith', 'Alice Smith', '1985-03-20', ARRAY['Java', 'C++', 'HTML']),
        ('bob_johnson', 'Bob Johnson', '1990-07-10', ARRAY['Python', 'Ruby', 'CSS']),
        ('emily_davis', 'Emily Davis', '1976-12-05', ARRAY['JavaScript', 'HTML', 'React']),
        ('michael_wilson', 'Michael Wilson', '1988-05-30', ARRAY['Java', 'C#', 'SQL']),
        ('emma_brown', 'Emma Brown', '1995-09-25', ARRAY['Python', 'JavaScript', 'Angular']),
        ('james_miller', 'James Miller', '1983-08-12', ARRAY['C++', 'PHP', 'HTML']),
        ('olivia_taylor', 'Olivia Taylor', '1987-04-18', ARRAY['Java', 'Python', 'React']),
        ('william_moore', 'William Moore', '1974-11-08', ARRAY['JavaScript', 'CSS', 'Node.js']),
        ('sophia_anderson', 'Sophia Anderson', '1992-02-28', ARRAY['Python', 'Java', 'SQL']);
END; $$
