-- This script converts hbtn_0c_0 database to UTF8
ALTER DATABASE hbtn_0c_0 COLLATE utf8mb4_unicode_ci; 
ALTER TABLE first_table (
    name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
) CHARACTER SET utf8mb4;
