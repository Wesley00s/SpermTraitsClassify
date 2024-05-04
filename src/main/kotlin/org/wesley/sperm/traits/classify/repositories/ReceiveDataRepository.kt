package org.wesley.sperm.traits.classify.repositories

import org.springframework.data.jpa.repository.JpaRepository
import org.wesley.sperm.traits.classify.model.Data

interface ReceiveDataRepository : JpaRepository<Data, Long>