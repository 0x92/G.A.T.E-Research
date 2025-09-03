import React, { useEffect, useState } from 'react';
import Timeline from 'react-calendar-timeline';
import moment from 'moment';
import 'react-calendar-timeline/dist/style.css';

function EventTimeline() {
  const [items, setItems] = useState([]);

  const groups = [
    { id: 1, title: 'Threads' },
    { id: 2, title: 'Publications' },
    { id: 3, title: 'Persons' }
  ];

  useEffect(() => {
    const load = async () => {
      try {
        const res = await fetch('/data/index.json');
        if (!res.ok) return;
        const docs = await res.json();
        const timelineItems = docs.slice(0, 100).map((doc, idx) => {
          const start = doc.date ? moment(doc.date) : moment();
          let group = 2;
          if (doc.filePath && doc.filePath.toLowerCase().includes('thread')) {
            group = 1;
          } else if (doc.entities && doc.entities.length > 0) {
            group = 3;
          }
          return {
            id: idx + 1,
            group,
            title: doc.title || doc.filePath,
            start_time: start,
            end_time: start.clone().add(1, 'hour'),
            itemProps: { 'data-url': doc.filePath }
          };
        });
        setItems(timelineItems);
      } catch (err) {
        console.error(err);
      }
    };
    load();
  }, []);

  const handleItemClick = (itemId) => {
    const item = items.find((i) => i.id === itemId);
    if (item) {
      const url = item.itemProps['data-url'];
      if (url) {
        const link = url.startsWith('http') ? url : `/${url}`;
        window.open(link, '_blank');
      }
    }
  };

  return (
    <div>
      <Timeline
        groups={groups}
        items={items}
        onItemClick={handleItemClick}
        defaultTimeStart={moment().add(-1, 'month')}
        defaultTimeEnd={moment().add(1, 'month')}
      />
    </div>
  );
}

export default EventTimeline;
