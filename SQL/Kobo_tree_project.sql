DROP DATABASE IF EXISTS greenwatch_db;

CREATE DATABASE greenwatch_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
USE greenwatch_db;


-- 1. Lookup tables ----------------------------------------------------------
CREATE TABLE IF NOT EXISTS entities (
  id INT AUTO_INCREMENT PRIMARY KEY,
  entity_type VARCHAR(100) NOT NULL,    -- e.g., NGO, Government, Individual
  entity_name VARCHAR(255) NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS locations (
  id INT AUTO_INCREMENT PRIMARY KEY,
  state VARCHAR(100) NULL,
  lga VARCHAR(100) NULL,
  ward VARCHAR(100) NULL,
  community VARCHAR(255) NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY ux_location(state, lga, ward, community)
);

CREATE TABLE IF NOT EXISTS species (
  id INT AUTO_INCREMENT PRIMARY KEY,
  species_name VARCHAR(255) NOT NULL,
  common_name VARCHAR(255) NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY ux_species(species_name)
);

CREATE TABLE IF NOT EXISTS threat_types (
  id INT AUTO_INCREMENT PRIMARY KEY,
  threat_name VARCHAR(200) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY ux_threat(threat_name)
);

-- 2. Baseline table --------------------------------------------------------
CREATE TABLE IF NOT EXISTS baseline_trees (
  id INT AUTO_INCREMENT PRIMARY KEY,
  tree_uuid VARCHAR(128) NOT NULL UNIQUE,     -- Tree ID from KoBo (scoped unique)
  submission_id VARCHAR(128) NULL,            -- KoBo _id/_uuid if different
  submitted_at DATETIME NULL,                 -- KoBo _submission_time
  entity_id INT NULL,                         -- FK to entities
  entity_type_other VARCHAR(255) NULL,        -- free text when 'Other'
  location_id INT NULL,                       -- FK to locations
  community VARCHAR(255) NULL,
  planting_date DATE NULL,
  species_id INT NULL,                        -- FK to species
  species_other VARCHAR(255) NULL,
  tree_count INT NULL,
  planted_by VARCHAR(255) NULL,
  initial_condition VARCHAR(100) NULL,
  notes TEXT NULL,
  latitude DOUBLE NULL,
  longitude DOUBLE NULL,
  altitude DOUBLE NULL,
  gps_accuracy FLOAT NULL,
  raw_json JSON NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_baseline_entity FOREIGN KEY (entity_id) REFERENCES entities(id) ON DELETE SET NULL,
  CONSTRAINT fk_baseline_location FOREIGN KEY (location_id) REFERENCES locations(id) ON DELETE SET NULL,
  CONSTRAINT fk_baseline_species FOREIGN KEY (species_id) REFERENCES species(id) ON DELETE SET NULL
);

CREATE INDEX idx_baseline_treeuuid ON baseline_trees(tree_uuid);
CREATE INDEX idx_baseline_location ON baseline_trees(location_id);
CREATE INDEX idx_baseline_species ON baseline_trees(species_id);

-- 3. Monitoring table ------------------------------------------------------
CREATE TABLE IF NOT EXISTS monitoring_reports (
  id INT AUTO_INCREMENT PRIMARY KEY,
  monitoring_uuid VARCHAR(128) NULL,         -- KoBo monitoring submission identifier
  submission_id VARCHAR(128) NULL,           -- KoBo _id/_uuid
  baseline_id INT NULL,                      -- FK to baseline_trees.id
  submitted_at DATETIME NULL,
  visit_date DATE NULL,
  monitoring_entity_id INT NULL,             -- FK to entities
  monitoring_entity_other VARCHAR(255) NULL,
  location_id INT NULL,                      -- location at time of visit (can update)
  latitude DOUBLE NULL,
  longitude DOUBLE NULL,
  altitude DOUBLE NULL,
  gps_accuracy FLOAT NULL,
  current_condition VARCHAR(100) NULL,
  current_condition_other VARCHAR(255) NULL,
  watered_recently BOOLEAN NULL,
  watered_details VARCHAR(255) NULL,
  pest_disease BOOLEAN NULL,
  pest_disease_notes VARCHAR(255) NULL,
  threat_other VARCHAR(255) NULL,
  protective_measures TEXT NULL,
  recommended_action TEXT NULL,
  recommended_action_other VARCHAR(255) NULL,
  recommend_expert_intervention BOOLEAN NULL,
  expert_reason TEXT NULL,
  final_remarks TEXT NULL,
  raw_json JSON NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_monitor_baseline FOREIGN KEY (baseline_id) REFERENCES baseline_trees(id) ON DELETE SET NULL,
  CONSTRAINT fk_monitor_entity FOREIGN KEY (monitoring_entity_id) REFERENCES entities(id) ON DELETE SET NULL,
  CONSTRAINT fk_monitor_location FOREIGN KEY (location_id) REFERENCES locations(id) ON DELETE SET NULL
);

CREATE INDEX idx_monitor_baseline ON monitoring_reports(baseline_id);
CREATE INDEX idx_monitor_subtime ON monitoring_reports(submitted_at);

-- 4. Monitoring <-> Threats (many-to-many) ---------------------------------
CREATE TABLE IF NOT EXISTS monitoring_threats (
  id INT AUTO_INCREMENT PRIMARY KEY,
  monitoring_id INT NOT NULL,
  threat_type_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_mt_monitor FOREIGN KEY (monitoring_id) REFERENCES monitoring_reports(id) ON DELETE CASCADE,
  CONSTRAINT fk_mt_threat FOREIGN KEY (threat_type_id) REFERENCES threat_types(id) ON DELETE CASCADE,
  UNIQUE KEY ux_monitor_threat(monitoring_id, threat_type_id)
);

-- 5. Media table (photos, attachments) -------------------------------------
CREATE TABLE IF NOT EXISTS media (
  id INT AUTO_INCREMENT PRIMARY KEY,
  baseline_id INT NULL,
  monitoring_id INT NULL,
  media_type VARCHAR(50) NULL,   -- image, audio, video
  media_url VARCHAR(1024) NULL,
  filename VARCHAR(512) NULL,
  filesize INT NULL,
  caption VARCHAR(255) NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_media_baseline FOREIGN KEY (baseline_id) REFERENCES baseline_trees(id) ON DELETE CASCADE,
  CONSTRAINT fk_media_monitor FOREIGN KEY (monitoring_id) REFERENCES monitoring_reports(id) ON DELETE CASCADE
);

CREATE INDEX idx_media_baseline ON media(baseline_id);
CREATE INDEX idx_media_monitor ON media(monitoring_id);

# checking index on the table to comfirm index name.
SHOW INDEX FROM locations;
SHOW INDEX FROM species;
SHOW INDEX FROM threat_types;


# removing the unwated unique key for locations table only. species and threat_types remain same.
DROP INDEX ux_location ON locations;
SHOW INDEX FROM locations;




