# controllers/api_config.py

class APIConfig:
    # Base route config
    BASE_URL = '/api'
    VERSION = 'v1'

    # Pagination defaults
    DEFAULT_LIMIT = 20
    MAX_LIMIT = 100
    DEFAULT_OFFSET = 0

    # Response standard format keys
    STATUS_SUCCESS = 'success'
    STATUS_ERROR = 'error'

    @classmethod
    def get_full_url(cls, path: str):
        """
        Generates the full route for an endpoint.
        Example: /api/v1/leads
        """
        return f"{cls.BASE_URL}/{cls.VERSION}{path}"

    @classmethod
    def paginate(cls, records, offset=0, limit=20):
        """
        Paginate the given recordset manually.
        """
        total = len(records)
        offset = max(0, int(offset))
        limit = min(int(limit), cls.MAX_LIMIT)
        paginated = records[offset:offset+limit]
        return {
            "status": cls.STATUS_SUCCESS,
            "total": total,
            "offset": offset,
            "limit": limit,
            "count": len(paginated),
            "data": [r.read() for r in paginated],
        }
